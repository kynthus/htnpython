import java.sql.{Connection, DriverManager, PreparedStatement, ResultSet}
import java.util.Properties

import org.apache.flink.configuration.Configuration
import org.apache.flink.formats.json.JsonNodeDeserializationSchema
import org.apache.flink.shaded.jackson2.com.fasterxml.jackson.databind.node.ObjectNode
import org.apache.flink.streaming.api.TimeCharacteristic
import org.apache.flink.streaming.api.functions.AssignerWithPunctuatedWatermarks
import org.apache.flink.streaming.api.functions.source.{RichParallelSourceFunction, SourceFunction}
import org.apache.flink.streaming.api.watermark.Watermark
import org.apache.flink.streaming.api.windowing.assigners.TumblingEventTimeWindows
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer


final case class TestSource() extends RichParallelSourceFunction[(String, String, Double)] {

  private[this] var connection: Connection = _
  private[this] var statement: PreparedStatement = _

  override def open(parameters: Configuration): Unit = {
    Console.err.println("TestSource#open()")

    this.connection = DriverManager.getConnection(
      "jdbc:postgresql://localhost:5432/test",
      "postgres",
      "Rootpwd01!"
    )
    this.statement = this.connection.prepareStatement("SELECT * FROM guzai")

    super.open(parameters)
  }

  override def run(ctx: SourceFunction.SourceContext[(String, String, Double)]): Unit = {

    while (true) {

      Console.err.println("TestSource#run()")

      val result: ResultSet = this.statement.executeQuery()

      for (_ <- Iterator.continually(result.next()).takeWhile(locally)) {

        ctx.collect(
          (
            result.getString("id"),
            result.getString("name"),
            result.getDouble("cal")
          )
        )

      }

      Thread.sleep(5000L)

    }

  }

  override def close(): Unit = {
    Console.err.println("TestSource#close()")

    if (this.statement != null && this.statement.isClosed) {
      this.statement.cancel()
    }
    if (this.connection != null && !this.connection.isClosed) {
      this.connection.close()
    }

    super.close()
  }

  override def cancel(): Unit = {
    Console.err.println("TestSource#cancel()")
  }

}


senv.setStreamTimeCharacteristic(TimeCharacteristic.EventTime)

val sourceProps: Properties = new Properties()
sourceProps.setProperty(
  "bootstrap.servers",
  "localhost:9092"
)

val consumer: SourceFunction[ObjectNode] = new FlinkKafkaConsumer(
  "test-onigilist",
  new JsonNodeDeserializationSchema(),
  sourceProps
).assignTimestampsAndWatermarks {
  new AssignerWithPunctuatedWatermarks[ObjectNode] {

    override final def checkAndGetNextWatermark(lastElement: ObjectNode, extractedTimestamp: Long):
    Watermark = new Watermark(extractedTimestamp)

    override final def extractTimestamp(element: ObjectNode, previousElementTimestamp: Long):
    Long = System.currentTimeMillis()

  }
}

val customSource: SourceFunction[(String, String, Double)] = TestSource()

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

val guzai: DataStream[(String, String, Double)] = senv.addSource(customSource)
  .assignTimestampsAndWatermarks {
    new AssignerWithPunctuatedWatermarks[(String, String, Double)] {

      override final def checkAndGetNextWatermark
      (lastElement: (String, String, Double), extractedTimestamp: Long):
      Watermark = new Watermark(extractedTimestamp)

      override final def extractTimestamp
      (element: (String, String, Double), previousElementTimestamp: Long):
      Long = System.currentTimeMillis()

    }
  }

onigilist.join(guzai)
  .where { case (_, _, _, _, guzai_id) => guzai_id }
  .equalTo { case (id, _, _) => id }
  .window(TumblingEventTimeWindows.of(Time.seconds(5L)))(_ -> _)
  .print()

senv.execute()
