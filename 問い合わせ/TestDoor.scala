import java.util.Properties

import org.apache.flink.api.java.io.jdbc.JDBCOutputFormat
import org.apache.flink.api.scala.createTypeInformation
import org.apache.flink.formats.json.JsonNodeDeserializationSchema
import org.apache.flink.shaded.jackson2.com.fasterxml.jackson.databind.JsonNode
import org.apache.flink.shaded.jackson2.com.fasterxml.jackson.databind.node.ObjectNode
import org.apache.flink.streaming.api.functions.source.SourceFunction
import org.apache.flink.streaming.api.scala.StreamExecutionEnvironment
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer
import org.apache.flink.types.Row

object TestDoor extends AnyRef {

  final case class DoorData
  (
    stopID: String,
    stopName: String,
    status: Seq[String],
    obstacle: Seq[String],
    emergency: Seq[String]
  ) extends AnyRef {

    def toRow: Row = {

      val fields: Seq[_] = this.stopID +:
        this.stopName +:
        this.status ++:
        this.obstacle ++:
        this.emergency

      fields.zipWithIndex
        .foldLeft(new Row(fields.size)) {
          case (row, (value, index)) =>
            row.setField(index, value)
            row
        }

    }

  }

  final object DoorData extends AnyRef {

    def apply(node: ObjectNode): DoorData = {

      val doorData: JsonNode = node.get("door_data")
      val doors: Seq[JsonNode] = for (n <- 1 to doorData.size())
        yield doorData.get(f"ride_rate_$n%02d")

      DoorData(
        node.get("stop_id").asText(),
        node.get("stop_name").asText(),
        doors.map(_.get("status").asText()),
        doors.map(_.get("obstacle").asText()),
        doors.map(_.get("emergency").asText())
      )

    }

  }


  def main(args: Array[String]): Unit = {

    val senv: StreamExecutionEnvironment = StreamExecutionEnvironment.getExecutionEnvironment

    val sourceProps: Properties = new Properties()
    sourceProps.setProperty(
      "bootstrap.servers",
      "localhost:9092"
    )

    val consumer: SourceFunction[ObjectNode] = new FlinkKafkaConsumer(
      "test-door",
      new JsonNodeDeserializationSchema(),
      sourceProps
    )

    val outputJDBC: JDBCOutputFormat = JDBCOutputFormat.buildJDBCOutputFormat().
      setDrivername("org.postgresql.Driver").
      setDBUrl("jdbc:postgresql://localhost:5432/test").
      setUsername("postgres").
      setPassword("Psqlpwd01!").
      setQuery(
        """
          |INSERT INTO door_data
          |VALUES(?, ?,
          |?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
          |""".stripMargin
      ).
      setBatchInterval(0).
      finish()

    senv.addSource(consumer)
      .map(DoorData(_))
      .print()

  }

}
