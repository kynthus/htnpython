# -*- coding: utf-8 -*-

R"""
自前でリソース管理(RAII)
"""

from contextlib import contextmanager
from threading import Lock

from pyspark.sql import SparkSession


@contextmanager
def auto_lock(lock):
    R"""
    排他ロックを取得して一旦呼び出し元へ戻るが、最終的には必ず解放する
    :param  lock:   排他を取得するロック
    """
    # 排他ロックを取得
    lock.acquire()
    try:
        # ここで呼び出し元へ戻る
        yield
    finally:
        # 必ず排他ロックを解放する
        lock.release()


# 自動排他ロックの関数はwithとともに呼び出す
with auto_lock(lock=Lock()):
    print('Sync output.')


@contextmanager
def spark_management():
    R"""
    SparkSessionを生成して呼び元へ戻し、最後に必ず停止する
    """
    session = SparkSession.builder.getOrCreate()
    try:
        # 呼び元へSparkSessionを戻す
        yield session
    finally:
        # 必ずSparkSessionを停止する
        session.stop()


# 関数が生成したSparkSessionはasで受け取れる
with spark_management() as spark:
    spark.sparkContext.setLogLevel(logLevel='WARN')
    spark.read.text(path='test.txt').show()
