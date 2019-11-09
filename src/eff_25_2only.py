# -*- coding: utf-8 -*-

R"""
多重継承
★そもそもメソッドが被っている複数クラスは多重継承しない方がいい
"""


class YHVH(object):
    R"""
    アダム・イブを生み出した神
    """

    def __init__(self):
        pass

    def show(self):
        print('YHVH')


class Adam(YHVH):
    R"""
    神によって生み出された最初の男性
    """

    def __init__(self):
        super(Adam, self).__init__()

    def show(self):
        print('Adam')


class Eve(YHVH):
    R"""
    神によって生み出された最初の女性
    ※実際はアダムの肋骨から分身したらしい……
    """

    def __init__(self):
        super(Eve, self).__init__()

    def show(self):
        print('Eve')


class Cain(Adam, Eve):
    R"""
    アダムとイヴの長男
    """

    def __init__(self):
        super(Cain, self).__init__()


class Abel(Eve, Adam):
    R"""
    アダムとイヴの次男
    ※継承順がカインと違う点に注目
    """

    def __init__(self):
        super(Abel, self).__init__()


cain = Cain()
cain.show()  # ← 何が出てくるの?

# 正解は「Adam」
# Python 2.2 よりC3線形化アルゴリズムが採用
print(Cain.mro())

abel = Abel()
abel.show()  # こっちは「Eve」

# 呼び出されるメソッドは左側から順に探索される
# Scalaと探索方向が逆なので注意！
print(Abel.mro())
