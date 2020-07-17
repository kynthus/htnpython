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

object TestTrain extends AnyRef {

  final case class TrainData
  (
    tripID: String,
    latitude: Double,
    longitude: Double,
    rideRates: Seq[Double]
  ) extends AnyRef {

    // tripID + latitude + longitude + RideRateAverage + rideRates...
    private[this] val FieldCount = rideRates.size + 4

    private[this] val RideRateAverage: Double = rideRates.sum / rideRates.size

    def toRow: Row = {

      val fields: Seq[_] = this.tripID +:
        this.latitude +:
        this.longitude +:
        this.rideRates :+
        this.RideRateAverage

      fields.zipWithIndex
        .foldLeft(new Row(this.FieldCount)) {
          case (row, (value, index)) =>
            row.setField(index, value)
            row
        }

    }

  }

  final object TrainData extends AnyRef {

    def apply(node: ObjectNode): TrainData = {

      val vehicleData: JsonNode = node.get("vehicle_data")

      TrainData(
        node.get("trip_id").asText(),
        node.get("latitude").asDouble(),
        node.get("longitude").asDouble(),
        for (n <- 1 to vehicleData.size())
          yield vehicleData.get(f"ride_rate_$n%02d").asDouble()
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
      "test-topic",
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
          |INSERT INTO train_data
          |VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
          |""".stripMargin
      ).
      setBatchInterval(0).
      finish()

    senv.addSource(consumer)
      .map(TrainData(_))
      .print()

  }

}
