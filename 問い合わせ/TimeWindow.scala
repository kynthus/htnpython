import java.util.Properties

import org.apache.flink.api.scala.createTypeInformation
import org.apache.flink.formats.json.JsonNodeDeserializationSchema
import org.apache.flink.shaded.jackson2.com.fasterxml.jackson.databind.node.ObjectNode
import org.apache.flink.streaming.api.functions.source.SourceFunction
import org.apache.flink.streaming.api.scala.StreamExecutionEnvironment
import org.apache.flink.streaming.api.windowing.time.Time
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer

final case class MyRecord[Key, Value]
(
  key: Key,
  value: Value,
  timestamp: Long,
  valueLen: Int
) extends AnyRef

object MyRecord extends AnyRef {

  def apply(node: ObjectNode):
  MyRecord[String, String] = this (
    node.get("key").asText(),
    node.get("value").asText(),
    node.get("timestamp").asLong(),
    node.get("value").asText().length()
  )

}

val sourceProps: Properties = new Properties()
sourceProps.setProperty("bootstrap.servers", "localhost:9092")

val consumer: SourceFunction[ObjectNode] = new FlinkKafkaConsumer(
  "test-topic",
  new JsonNodeDeserializationSchema(),
  sourceProps
)

senv.addSource(consumer).
  map(MyRecord(_)).
  timeWindowAll(Time.seconds(5L)).
  sum("valueLen").
  map(_.valueLen).
  print()

senv.execute("Test...")
