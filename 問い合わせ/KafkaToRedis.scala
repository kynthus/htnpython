import java.util.Properties

import org.apache.flink.api.common.serialization.SimpleStringSchema
import org.apache.flink.api.scala.createTypeInformation
import org.apache.flink.streaming.api.functions.sink.SinkFunction
import org.apache.flink.streaming.api.functions.source.SourceFunction
import org.apache.flink.streaming.api.scala.{DataStream, StreamExecutionEnvironment}
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer
import org.apache.flink.streaming.connectors.redis.RedisSink
import org.apache.flink.streaming.connectors.redis.common.config.{FlinkJedisConfigBase, FlinkJedisPoolConfig}
import org.apache.flink.streaming.connectors.redis.common.mapper.{RedisCommand, RedisCommandDescription, RedisMapper}

object KafkaToRedis extends AnyRef {

  def main(args: Array[String]): Unit = {

    val sourceProps: Properties = new Properties()
    sourceProps.setProperty("bootstrap.servers", "localhost:9092")

    val source: SourceFunction[String] = new FlinkKafkaConsumer(
      "test-topic",
      new SimpleStringSchema(),
      sourceProps
    )

    val sinkProps: Properties = new Properties()
    sinkProps.setProperty("bootstrap.servers", "localhost:9092")

    val jedisCofig: FlinkJedisConfigBase = new FlinkJedisPoolConfig.Builder()
      .setHost("localhost")
      .build()

    val sink: SinkFunction[(String, String)] = new RedisSink(
      jedisCofig,
      new RedisExampleMapper(RedisCommand.SET)
    )

    val senv = StreamExecutionEnvironment.getExecutionEnvironment
    senv.setParallelism(1)

    val processing: DataStream[(String, String)] =
      for (s <- senv.addSource(source)) yield {
        val Array(key, value) = s.split(',')
        key -> value
      }

    processing.addSink(sink)

    senv.execute("Kafka consumer streaming.")

  }

  private[this] final class RedisExampleMapper
  (private[this] val redisCommand: RedisCommand)
    extends RedisMapper[(String, String)] {

    protected[this] override def getCommandDescription:
    RedisCommandDescription = new RedisCommandDescription(redisCommand, "")

    protected[this] override def getKeyFromData
    (data: (String, String)): String = {
      val (key, _) = data
      key
    }

    protected[this] override def getValueFromData
    (data: (String, String)): String = {
      val (_, value) = data
      value
    }

  }

}
