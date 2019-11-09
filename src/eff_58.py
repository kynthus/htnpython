# -*- coding: utf-8 -*-

R"""
プログラムの処理時間をプロファイリングする
"""

from cProfile import Profile
from pstats import Stats
from random import randint


def insertion_sort(data):
    R"""
    配列の挿入ソートを行う
    :param      data:   ソート対象となる配列
    :return:    ソート後の配列
    """
    result = []

    for value in data:
        insert_value(array=result, value=value)

    return result


def insert_value(array, value):
    R"""
    ソート済み配列へ値を挿入する
    :param  array:  挿入対象となる配列
    :param  value:  挿入する整数値
    """
    for i, existing in enumerate(array):

        if value < existing:
            array.insert(i, value)
            return

    array.append(value)


# ランダムな整数値を10000回生成する
max_size = 10 ** 4
randoms = [randint(0, max_size) for _ in range(max_size)]


def test():
    R"""
    10000個のランダムな整数値を挿入ソートする
    """
    insertion_sort(data=randoms)


# 挿入ソート処理を対象にプロファイリングを行う
profiler = Profile()
profiler.runcall(func=test)

# プロファイリングの統計を表示する
stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
