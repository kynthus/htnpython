# -*- coding: utf-8 -*-

R"""
concurrent.futureによる並列性
"""

from time import time

from concurrent.futures.process import ProcessPoolExecutor


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
    return list(factorize(number=number))


if __name__ == '__main__':
    numbers = [
        2139079, 1214759, 1516637, 1852285,
        2062547, 1587654, 2625139, 2474102,
    ]

    # マルチスレッドでの合計処理時間を算出(速くなるが、少量のデータであればの話)
    start = time()
    # 4CPUで並列実行するスレッドプールを作成
    pool = ProcessPoolExecutor(max_workers=4)
    results = list(pool.map(factorize_list, numbers))
    end = time()
    print('Took {} seconds'.format(end - start))
