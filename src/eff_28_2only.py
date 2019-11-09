# -*- coding: utf-8 -*-

R"""
カスタムコンテナの作成
"""

from collections import Sequence


class MyList(Sequence):
    R"""
    簡単な自作リスト(Sequenceを継承)
    """

    def __init__(self, *args):
        R"""
        可変引数でリストを初期化する
        :param  args:   可変長引数
        """
        self.args = args

    def __getitem__(self, item):
        R"""
        リストから要素を取得する
        :param      item:   取得する要素のインデックス
        :return:    引数に対応するリストの要素
        """
        return self.args[item]

    def __len__(self):
        R"""
        現在のリスト長さを返す
        :return:    現在のリスト長
        """
        return len(self.args)


ls = MyList(1, 2, 3, 4, 3)

# Sequenceを継承しているクラスは
# __getitem__()と__len__()を実装することで
# count()とindex()を自動的に実装できる
print(ls.count(3))
print(ls.index(4))
