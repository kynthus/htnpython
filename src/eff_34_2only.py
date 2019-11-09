# -*- coding: utf-8 -*-

R"""
クラスをメタクラスで登録
★さまざまなクラスに適用可能な機能に対し、メタクラスに手続きを書いて簡素化
"""

import json


class RegisterMeta(type):
    R"""
    エンコードクラスを登録するためのメタクラス
    """

    # エンコード可能なクラスを、クラス名とその属性値を持つことで管理する
    registry = {}

    def __new__(mcs, name, bases, class_dict):
        R"""
        クラス定義生成時に、エンコード可能なクラスとして登録する
        :param      name:       クラス名
        :param      bases:      基底クラスのタプル
        :param      class_dict: フィールドを記した辞書
        :return:    typeにより生成されたクラス定義
        """
        cls = super(RegisterMeta, mcs).__new__(mcs, name, bases, class_dict)

        # クラス定義生成の時点で、自動登録してしまう
        mcs.register_class(cls)

        return cls

    @classmethod
    def register_class(mcs, target_class):
        R"""
        クラスをエンコード可能クラスとして登録する
        :param  target_class:   登録するクラス
        """
        mcs.registry[target_class.__name__] = target_class


class Encoder(object):
    R"""
    派生クラスをJSON形式へエンコードする
    """
    __metaclass__ = RegisterMeta

    def __init__(self, *args):
        R"""
        派生クラスの属性値を設定する
        :param  args:   エンコード対象となる派生クラスの属性値
        """
        self.args = args

    def encode(self):
        R"""
        派生クラス名と属性値をJSONへ変換
        :return:    エンコードの結果として生成されたJSON
        """
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args,
        })  # dumps


def decode(data):
    R"""
    クラスをJSONよりデコードする
    :param      data:   デコード対象のJSON形式データ
    :return:    デコードの結果として生成されたインスタンス
    """
    # JSONを辞書へ変換
    params = json.loads(data)

    # 「class」フィールドのクラス名を探し、登録されているクラスを取得
    target_class = RegisterMeta.registry[params['class']]

    # 「args」フィールドの値を渡し、インスタンスを生成
    return target_class(*params['args'])


class Point2D(Encoder):
    R"""
    二次元座標
    """

    def __init__(self, x, y):
        R"""
        X座標とY座標をもとに生成
        :param  x:  X座標
        :param  y:  Y座標
        """
        super(Point2D, self).__init__(x, y)
        self.x = x
        self.y = y

    def __str__(self):
        R"""
        座標を文字列へ変換
        :return:    p(x, y)
        """
        return 'p({}, {})'.format(self.x, self.y)


class Vector3D(Encoder):
    R"""
    三次元ベクトル
    """

    def __init__(self, x, y, z):
        R"""
        X, Y, Z成分をもとに生成
        :param  x:  X成分
        :param  y:  Y成分
        :param  z:  Z成分
        """
        super(Vector3D, self).__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        R"""
        ベクトルを文字列へ変換
        :return:    T(x, y, z)
        """
        return 'T({}, {}, {})'.format(self.x, self.y, self.z)


# Point2Dのシリアライズ
pt2 = Point2D(x=1920, y=1080)
print('Before : {}'.format(pt2))
pt2_enc = pt2.encode()
print('Encoded: {}'.format(pt2_enc))
print('After  : {}'.format(decode(pt2_enc)))

# Vector3Dもシリアライズ可能
vec3 = Vector3D(x=10, y=-7, z=3)
print('Before : {}'.format(vec3))
vec3_enc = vec3.encode()
print('Encoded: {}'.format(vec3_enc))
print('After  : {}'.format(decode(vec3_enc)))
