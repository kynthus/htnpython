# -*- coding: utf-8 -*-

R"""
派生クラスをメタクラスで検証する
★派生クラスが要件を満たしているかを定義段階でチェック
"""


class AnimalMeta(type):
    R"""
    動物のメタクラス
    """

    def __new__(mcs, name, bases, class_dict):
        R"""
        メタデータよりクラスを生成する
        ただし四足歩行の動物のみ許可する
        :param      name:
        :param      bases:
        :param      class_dict:
        :return:    メタデータより生成したクラス
        """
        if bases != (object,) and class_dict['legs'] != 4:
            raise ValueError('My Animal is 4 legs just!')

        return super(AnimalMeta, mcs).__new__(mcs, name, bases, class_dict)


class Animal(object):
    R"""
    さまざまな動物の基底クラス
    """
    __metaclass__ = AnimalMeta
    legs = None


class Dog(Animal):
    R"""
    犬は四足歩行なのでOK
    """
    legs = 4


class Cat(Animal):
    R"""
    猫も四足歩行なのでOK
    """
    legs = 4


class Giraffe(Animal):
    R"""
    同様にキリンも四足歩行なのでOK
    """
    legs = 4


class Human(Animal):
    R"""
    ヒトは二足歩行なのでNG
    ※Humanクラスは定義した時点でエラー扱い
    """
    legs = 2


class Ant(Animal):
    R"""
    アリは六足なのでNG
    ※つまりは昆虫系全般が弾かれる
    """
    legs = 6
