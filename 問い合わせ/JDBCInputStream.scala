import java.util.Properties

import org.apache.flink.api.common.serialization.SimpleStringSchema
import org.apache.flink.api.java.io.jdbc.JDBCOutputFormat
import org.apache.flink.api.scala.createTypeInformation
import org.apache.flink.streaming.api.functions.source.SourceFunction
import org.apache.flink.streaming.api.scala.{DataStream, StreamExecutionEnvironment}
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer
import org.apache.flink.types.Row

val sourceProps: Properties = new Properties()
sourceProps.setProperty("bootstrap.servers", "localhost:9092")

val consumer: SourceFunction[String] = new FlinkKafkaConsumer(
  "test-topic",
  new SimpleStringSchema(),
  sourceProps
)

val outputJDBC: JDBCOutputFormat = JDBCOutputFormat.buildJDBCOutputFormat().
  setDrivername("org.postgresql.Driver").
  setDBUrl("jdbc:postgresql://localhost:5432/test").
  setUsername("postgres").
  setPassword("Psqlpwd01!").
  setQuery("INSERT INTO student VALUES(?, ?, ?)").
  setBatchInterval(1).
  finish()

val records: DataStream[Row] = for (line <- senv.addSource(consumer)) yield {
  line.split(',') match {
    case Array(id, name, money) =>
      val row: Row = new Row(3)
      row.setField(0, id)
      row.setField(1, name)
      row.setField(2, BigDecimal(money))
      row
  }
}

records.writeUsingOutputFormat(outputJDBC)

senv.execute()
