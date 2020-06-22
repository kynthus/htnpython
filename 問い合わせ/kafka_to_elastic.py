from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import DataTypes, StreamTableEnvironment
from pyflink.table.descriptors import Csv, Json, Schema, Kafka, Elasticsearch

if __name__ == '__main__':
    s_env = StreamExecutionEnvironment.get_execution_environment()
    s_env.set_parallelism(1)

    st_env = StreamTableEnvironment.create(s_env)

    input_connector = Kafka() \
        .version('universal') \
        .topic('test-topic') \
        .property('bootstrap.servers', 'localhost:9092')

    input_format = Csv() \
        .field_delimiter(',')

    input_schema = Schema() \
        .field('word', DataTypes.STRING())

    st_env.connect(input_connector) \
        .with_format(input_format) \
        .with_schema(input_schema) \
        .create_temporary_table('words')

    output_connector = Elasticsearch() \
        .version('7') \
        .host('localhost', 9200, 'http') \
        .index('from-kafka') \
        .document_type('_doc') \
        .failure_handler_fail() \
        .bulk_flush_max_actions(3) \
        .bulk_flush_interval(1000)

    output_format = Json() \
        .fail_on_missing_field(True)

    output_schema = Schema() \
        .field('word', DataTypes.STRING())

    st_env.connect(output_connector) \
        .with_format(output_format) \
        .with_schema(output_schema) \
        .in_append_mode() \
        .create_temporary_table('wordcount')

    st_env.scan('words') \
        .select('*') \
        .insert_into('wordcount')

    st_env.execute('PyFlink Kafka Test')
