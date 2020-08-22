import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import java.io.IOException;
import java.util.StringTokenizer;

/**
 * テキストファイルのコピーを行うMapReduceアプリケーション
 */
public class MapReduceTest {

    /**
     * HDFS上のテキストファイルをコピーする
     *
     * @param args 配列の0番目に入力元ファイルパス、1番目に出力先ディレクトリパスが格納される
     * @throws IOException            MapReduceを実行するフレームワークとの通信に失敗した場合
     * @throws ClassNotFoundException MapReduce実行中にクラスのロードに失敗した場合
     * @throws InterruptedException   何らかの割り込み処理が発生した場合
     */
    public static void main(String[] args)
        throws IOException, ClassNotFoundException, InterruptedException {

        // 入力元ファイルパスと出力先ディレクトリが指定されていない場合はエラー扱い
        if (args.length < 2) {
            System.err.println("Usage: MapReduceTest.jar <入力元ファイルパス> <出力先ディレクトリパス>");
            System.exit(1);
        }

        // MapReduceアプリを実行するため、ジョブのインスタンスを取得
        Job job = Job.getInstance();

        // MapReduceTestをアプリケーションとして動かすよう指定
        job.setJarByClass(MapReduceTest.class);

        // Mapper, Combiner, Reducerへそれぞれテスト用を指定
        job.setMapperClass(TestMapper.class);
        job.setCombinerClass(TestReducer.class);
        job.setReducerClass(TestReducer.class);

        // 出力するキーと値のデータ型を指定
        job.setOutputKeyClass(NullWritable.class);
        job.setOutputValueClass(Text.class);

        // 入力元ファイルパスと出力先ディレクトリパスを指定
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        // MapReduceアプリを実行し、完了するまで待機する
        boolean isSuccess = job.waitForCompletion(true);

        // 成功した場合は0、失敗した場合は1でプログラムを終了する
        System.exit(isSuccess ? 0 : 1);

    }

    /**
     * テスト用のMapperクラス
     * <p>
     * テキストファイルから読み込んだ文字列を値として書き込み、Reducerへ渡す<br>
     * キーは未使用のため`NullWritable`とした<br>
     */
    private static final class TestMapper extends Mapper<LongWritable, Text, NullWritable, Text> {

        /**
         * テキストファイルから読み込んだ文字列の格納先
         */
        private final Text text = new Text();

        /**
         * テキストファイルから読み込んだ文字列を値として書き込む
         *
         * @param key     キー(未使用)
         * @param value   テキストファイルから読み込んだ文字列が入る
         * @param context Mapperが出力するペアを書き込むためのコンテキスト
         * @throws IOException          キーと値のペアの書き込みで入出力エラーが発生した場合
         * @throws InterruptedException 何らかの割り込み処理が発生した場合
         */
        @Override
        protected void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {

            // 読み込んだ文字列を文字列トークンとして解釈
            StringTokenizer tokenizer = new StringTokenizer(value.toString());

            // 文字列トークンが無くなるまで書き込みを繰り返す
            while (tokenizer.hasMoreTokens()) {

                // 1行分の文字列に改行文字を付与し、キー無しでコンテキストへ書き込む
                this.text.set(tokenizer.nextToken() + System.getProperty("line.separator"));
                context.write(NullWritable.get(), this.text);

            }

        }

    }

    /**
     * テスト用のReducerクラス
     * <p>
     * Reducerから受け取った文字列をコピー先テキストファイルへ書き込む<br>
     * キーは未使用のため`NullWritable`とした<br>
     */
    private static final class TestReducer extends Reducer<NullWritable, Text, NullWritable, Text> {

        /**
         * コピー先となるテキストファイルへ、書き込む文字列の格納先
         */
        private final Text result = new Text();

        /**
         * Mapperから渡された文字列を連結してテキストファイルへ書き込む
         *
         * @param key     Mapperから渡されたキー(未使用)
         * @param values  Mapperから渡されたキーに対応する値
         * @param context コピー先テキストファイルへ書き込むためのコンテキスト
         * @throws IOException          キーと値のペアの書き込みで入出力エラーが発生した場合
         * @throws InterruptedException 何らかの割り込み処理が発生した場合
         */
        @Override
        protected void reduce(NullWritable key, Iterable<Text> values, Context context)
            throws IOException, InterruptedException {

            // Mapperから渡された値を連結する
            StringBuilder builder = new StringBuilder();
            for (Text value : values) {
                builder.append(value);
            }

            // 連結した文字列をコピー先テキストファイルへ書き込む
            this.result.set(builder.toString());
            context.write(key, this.result);

        }

    }

}
