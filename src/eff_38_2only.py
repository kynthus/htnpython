# -*- coding: utf-8 -*-

R"""
マルチスレッド使用時の同期処理
"""

from threading import Lock, Thread
from time import sleep

# print時の排他用ロック
lock = Lock()


def sync_print(message):
    R"""
    サーバ側・クライアント側で表示が壊れないよう、同期する
    :param  message:    表示するオブジェクト
    """
    with lock:
        print(message)


def need_eraser():
    R"""
    消しゴムを貸してもらいたい関数
    """
    for i in range(10):
        sync_print('Can you lend me your eraser?')
        sleep(1.0)


def request_refuse():
    R"""
    絶対に消しゴムを貸したくない関数
    """
    for i in range(10):
        sync_print('Shut up!')
        sleep(1.0)


# 貸してもらいたい方は別スレッドで
need = Thread(target=need_eraser)
need.start()

# 拒否する方はメインスレッドで
request_refuse()
need.join()

print('Below infinite loop...')
