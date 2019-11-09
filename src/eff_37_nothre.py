# -*- coding: utf-8 -*-

R"""
Pythonスレッドによる並列性の恩恵(スレッドなし)
"""
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


numbers = [
    2139079, 1214759, 1516637, 1852285,
    2062547, 1587654, 2625139, 2474102,
]
start = time()
for n in numbers:
    list(factorize(number=n))
end = time()
print('Took {} seconds'.format(end - start))
