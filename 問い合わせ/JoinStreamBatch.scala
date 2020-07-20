import java.util.Properties

import org.apache.flink.api.java.io.jdbc.JDBCInputFormat
import org.apache.flink.api.java.typeutils.RowTypeInfo
import org.apache.flink.api.scala.typeutils.Types
import org.apache.flink.formats.json.JsonNodeDeserializationSchema
import org.apache.flink.shaded.jackson2.com.fasterxml.jackson.databind.node.ObjectNode
import org.apache.flink.streaming.api.functions.source.SourceFunction
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer
import org.apache.flink.table.api.Table


final case class JoinedRecord
(
  id: String,
  name: String,
  brand: String,
  price: Double,
  guzaiName: String,
  calorie: Double
) extends AnyRef

final object JoinedRecord extends AnyRef {

  def apply(row: Row): JoinedRecord = {

    val fields: Seq[_] = for (i <- 0 until row.getArity) yield row.getField(i)

    fields match {
      case Seq(
      id: String,
      name: String,
      brand: String,
      price: Double,
      _,
      _,
      guzaiName: String,
      calorie: Double
      ) => this (id, name, brand, price, guzaiName, calorie)

      case _ =>
        sys.error("Invalid record...")

    }

  }

}


val sourceProps: Properties = new Properties()
sourceProps.setProperty(
  "bootstrap.servers",
  "localhost:9092"
)

val consumer: SourceFunction[ObjectNode] = new FlinkKafkaConsumer(
  "test-onigilist",
  new JsonNodeDeserializationSchema(),
  sourceProps
)

val inputJDBC: JDBCInputFormat = JDBCInputFormat.buildJDBCInputFormat().
  setDrivername("org.postgresql.Driver").
  setDBUrl("jdbc:postgresql://localhost:5432/test").
  setUsername("postgres").
  setPassword("Rootpwd01!").
  setRowTypeInfo {
    new RowTypeInfo(
      Types.STRING,
      Types.STRING,
      Types.DOUBLE
    )
  }.
  setQuery("SELECT * FROM guzai").
  finish()

val onigilist: DataStream[(String, String, String, Double, String)] =
  for (json <- senv.addSource(consumer)) yield {
    (
      json.get("id").asText(),
      json.get("name").asText(),
      json.get("brand").asText(),
      json.get("price").asDouble(),
      json.get("guzai_id").asText()
    )
  }
val guzai: DataStream[Row] = senv.createInput(inputJDBC)

stenv.createTemporaryView(
  "onigilist",
  onigilist,
  'id,
  'onigili_name,
  'brand,
  'price,
  'guzai_id
)
stenv.createTemporaryView(
  "guzai",
  guzai,
  'foreign_guzai_id,
  'guzai_name,
  'cal
)

val onigilistTable: Table = stenv.from("onigilist")
val guzaiTable: Table = stenv.from("guzai")

val joinedTable: Table = onigilistTable.join(guzaiTable, "guzai_id = foreign_guzai_id")
val joinedStream: DataStream[Row] = stenv.toAppendStream(joinedTable)

joinedStream.map(JoinedRecord(_))
  .timeWindowAll(Time.seconds(10L))
  .max("calorie")
  .map(r => s"Has the highest calories ${r.calorie}")
  .print()

senv.execute()
