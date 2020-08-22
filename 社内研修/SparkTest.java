import org.apache.spark.SparkContext;
import org.apache.spark.rdd.RDD;
import org.apache.spark.sql.SparkSession;

/**
 * テキストファイルのコピーを行うSparkアプリケーション
 */
public class SparkTest {

    /**
     * HDFS上のテキストファイルをコピーする
     *
     * @param args 配列の0番目に入力元ファイルパス、1番目に出力先ディレクトリパスが格納される
     */
    public static void main(String[] args) {

        // 入力元ファイルパスと出力先ディレクトリが指定されていない場合はエラー扱い
        if (args.length < 2) {
            System.err.println("Usage: SparkTest.jar <入力元ファイルパス> <出力先ディレクトリパス>");
            System.exit(1);
        }

        // SparkSessionはリソース管理が必要なので、はじめにnullで初期化
        SparkSession spark = null;

        // SparkSessionは最後確実に停止するため、try-finally文を用いる
        try {

            // SparkSessionの生成
            spark = SparkSession.builder().getOrCreate();

            // 生成したSparkSessionより、SparkContextを取得
            SparkContext sc = spark.sparkContext();

            // テキストファイルを読み込む
            RDD<String> textFile = sc.textFile(args[0], 1);

            // 読み込んだ全行をHDFS上のファイルとして作成し、出力先ディレクトリへ配置する
            textFile.saveAsTextFile(args[1]);

        } finally {

            // SparkSessionが生成されている場合は停止する
            if (spark != null) {
                spark.stop();
            }

        }

    }

}
