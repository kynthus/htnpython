# -*- coding: utf-8 -*-

R"""
クラスメソッド
"""


class MySeq(object):
    R"""
    自作シーケンスのルートクラス
    """

    def __init__(self, *args):
        R"""
        シーケンスの各要素を文字列として保持する
        :param  args:   保持するシーケンス
        """
        self.seq = [str(e) for e in args]

    def __str__(self):
        R"""
        シーケンスをカンマ(',')区切りで文字列へ変換する
        :return:    文字列へ変換したシーケンス
        """
        return ','.join(self.seq)

    @classmethod
    def create_12345(cls):
        R"""
        1,2,3,4,5の連番で初期化したシーケンスを返す
        ただし、値は派生クラスのコンストラクタ次第で変化する
        :return:    1,2,3,4,5で初期化したシーケンス
        """
        return cls(1, 2, 3, 4, 5)


class DoubleSeq(MySeq):
    R"""
    各要素を2倍して保持するシーケンス
    """

    def __init__(self, *args):
        R"""
        各要素を2倍して基底クラスのコンストラクタへ渡す
        :param  args:   2倍するシーケンス
        """
        super(DoubleSeq, self).__init__(*[e * 2 for e in args])


class ReverseSeq(MySeq):
    R"""
    各要素を逆順にして保持するシーケンス
    """

    def __init__(self, *args):
        R"""
        各要素を逆順にして基底クラスのコンストラクタへ渡す
        :param  args:   逆順にするシーケンス
        """
        super(ReverseSeq, self).__init__(*reversed(list(args)))


# 2倍するシーケンスは[2,4,6,8,10]となる
print(DoubleSeq.create_12345())

# 逆順にするシーケンスは[5,4,3,2,1]となる
print(ReverseSeq.create_12345())
