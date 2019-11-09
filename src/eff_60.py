# -*- coding: utf-8 -*-

R"""
Pythonにおけるクラスの正体
"""


class AutoTest(object):
    R"""
    従来のクラス定義
    """

    def __init__(self):
        R"""
        コンストラクタによるフィールドの初期化
        """
        self.attr_A = 123
        self.attr_B = 456


# type関数を用いてクラスを定義
# クラスはこうして作られている
ManualTest = type(
    'ManualTest',
    (object,),
    {
        'attr_A': 123,
        'attr_B': 456,
    },  # {}
)  # type

# 従来のクラス生成とその属性値の取得
aut_test = AutoTest()

print(aut_test.attr_A)
print(aut_test.attr_B)

# type関数で書かれたクラスを使う
man_test = ManualTest()

print(man_test.attr_A)
print(man_test.attr_B)
