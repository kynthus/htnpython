# -*- coding: utf-8 -*-

R"""
イテレータオブジェクト
"""

import string


class AlphaIter(object):
    R"""
    自作の大文字アルファベットイテレータ
    """

    def __iter__(self):
        R"""
        イテレータオブジェクトに必要なメソッド
        :return:    [A-Z]までのアルファベットを1文字ずつ
        """
        for x in string.ascii_uppercase:
            yield x


# アルファベットイテレータを生成
alpha = AlphaIter()

# __iter__()を実装したクラスは、forの対象とすることができる
# [A-Z]までの文字を表示する
for c in alpha:
    print(c)
