# -*- coding: utf-8 -*-
import sys

from pyspark import SparkContext, RDD
from pyspark.sql import SparkSession

# HDFS上のテキストファイルをコピーする
if __name__ == '__main__':

    # 入力元ファイルパスと出力先ディレクトリが指定されていない場合はエラー扱い
    if len(sys.argv) <= 2:
        sys.stderr.writelines('Usage: pyspark_test.py <入力元ファイルパス> <出力先ディレクトリパス>')
        sys.exit(1)

    # SparkSessionを生成し、最終的に必ず停止する
    with SparkSession.builder.getOrCreate() as spark:  # type: SparkSession

        # 生成したSparkSessionより、SparkContextを取得
        sc = spark.sparkContext  # type: SparkContext

        # テキストファイルを読み込む
        text_file = sc.textFile(sys.argv[1])  # type: RDD

        # 読み込んだ全行をHDFS上のファイルとして作成し、出力先ディレクトリへ配置する
        text_file.saveAsTextFile(sys.argv[2])
