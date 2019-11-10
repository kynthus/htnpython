# -*- coding: utf-8 -*-

R"""
クラスデコレータ
"""


def need_4legs(cls):
    R"""
    メタデータよりクラスを生成する
    ただし四足歩行の動物のみ許可する
    :param      cls:    デコレート対象のクラス
    :return:    デコレート対象のクラス
    """
    if cls.__bases__ != (object,) and cls.__dict__['legs'] != 4:
        raise ValueError('My Animal is 4 legs just!')

    return cls


@need_4legs
class Animal(object):
    R"""
    さまざまな動物の基底クラス
    """
    legs = None


@need_4legs
class Dog(Animal):
    R"""
    犬は四足歩行なのでOK
    """
    legs = 4


@need_4legs
class Cat(Animal):
    R"""
    猫も四足歩行なのでOK
    """
    legs = 4


@need_4legs
class Giraffe(Animal):
    R"""
    同様にキリンも四足歩行なのでOK
    """
    legs = 4


@need_4legs
class Human(Animal):
    R"""
    ヒトは二足歩行なのでNG
    ※Humanクラスは定義した時点でエラー扱い
    """
    legs = 2


@need_4legs
class Ant(Animal):
    R"""
    アリは六足なのでNG
    ※つまりは昆虫系全般が弾かれる
    """
    legs = 6
