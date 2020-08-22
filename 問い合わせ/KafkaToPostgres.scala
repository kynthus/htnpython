import java.util.Properties

import org.apache.flink.api.scala.createTypeInformation
import org.apache.flink.configuration.Configuration
import org.apache.flink.formats.json.JsonNodeDeserializationSchema
import org.apache.flink.shaded.jackson2.com.fasterxml.jackson.databind.node.ObjectNode
import org.apache.flink.streaming.api.functions.sink.{RichSinkFunction, SinkFunction}
import org.apache.flink.streaming.api.functions.source.SourceFunction
import org.apache.flink.streaming.api.scala.StreamExecutionEnvironment
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer
import redis.clients.jedis.Jedis

import scala.collection.JavaConverters.asScalaIteratorConverter

object KafkaToPostgres extends AnyRef {

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

    val sink: SinkFunction[ObjectNode] = RedisCustomSink(
      host = "localhost",
      port = 6379,
      password = "Redispwd01!"
    )

    senv.addSource(consumer).addSink(sink)

  }

  private[this] final case class RedisCustomSink
  (
    private val host: String,
    private val port: Int,
    private val password: String
  ) extends RichSinkFunction[ObjectNode] {

    private[this] var jedis: Jedis = _

    override def open(parameters: Configuration): Unit = {

      this.jedis = new Jedis(this.host, this.port)
      this.jedis.auth(this.password)

    }

    override def invoke(input: ObjectNode, context: SinkFunction.Context[_]): Unit = {

      for (pair <- input.fields().asScala)
        this.jedis.set(pair.getKey, pair.getValue.asText())

    }

    override def close(): Unit = {

      if (this.jedis != null) {
        this.jedis.close()
      }

    }

  }

}
