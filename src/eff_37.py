# -*- coding: utf-8 -*-

R"""
Pythonスレッドによる並列性の恩恵(スレッドあり)
"""

from threading import Thread
from time import time


def factorize(number):
    R"""
    素因数分解を行う関数
    :param      number: 分解対象の整数値
    :return:    numberを割り切れる数
    """
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


def factorize_list(number):
    R"""
    素因数分解算出箇所をマルチスレッド化する際のメインパス
    :param  number: 分解対象の整数値
    """
    list(factorize(number=number))


numbers = [
    2139079, 1214759, 1516637, 1852285,
    2062547, 1587654, 2625139, 2474102,
]

# 各整数値の素因数分解スレッドを生成
threads = [Thread(target=factorize_list, args=[n]) for n in numbers]

# マルチスレッドでの合計処理時間を算出(速くはならない)
start = time()
for t in threads:
    t.start()
for t in threads:
    t.join()
end = time()
print('Took {} seconds'.format(end - start))
