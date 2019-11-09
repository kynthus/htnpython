# -*- coding: utf-8 -*-

R"""
関数オブジェクト(__call__メソッド)
"""


class Greet(object):
    R"""
    関数オブジェクトとして呼出可能なクラス
    """

    def __init__(self, name):
        R"""
        名前を受け取り初期化する
        :param  name:   名前
        """
        self.name = name

    def __call__(self, first):
        R"""
        __call__()を定義すると関数オブジェクトとして呼び出せる
        :param      first:  はじめに入れる挨拶
        """
        print('{}, {}!'.format(first, self.name))


# はじめにインスタンス生成
greet = Greet('FuncObj')

# インスタンスをさも関数のように呼び出せる
greet('Hello')
greet('Bye')
