# -*- coding: utf-8 -*-

R"""
クラス属性の注釈
例えばO/Rマッピング時に属性とカラムを紐付けしたいときなど
"""


class Attribute(object):
    R"""
    属性値を表す注釈用のクラス
    """

    def __init__(self):
        R"""
        外部用・内部用の双方をNoneへ設定(後で設定するので値は不要)
        """
        self.name = None
        self.internal_name = None

    def __get__(self, instance, instance_type):
        R"""
        インスタンスよりディスクリプタを取得する
        :param      instance:       ディスクリプタを取得するインスタンス
        :param      instance_type:  ディスクリプタのデータ型
        :return:    取得したディスクリプタ
        """
        if instance is None:
            return self

        return getattr(instance, self.internal_name, instance_type)

    def __set__(self, instance, value):
        R"""
        インスタンスに対してディスクリプタを設定する
        :param      instance:   設定対象のインスタンス
        :param      value:      設定する値
        """
        setattr(instance, self.internal_name, value)


class RowMeta(type):
    R"""
    属性値を持つクラスを生成するためのメタクラス
    メタクラスの場合はtypeを継承する
    """

    def __new__(mcs, name, bases, class_dict):
        R"""
        渡された情報を元に手動でクラスを生成する
        :param      name:       クラス名
        :param      bases:      基底クラスのタプル
        :param      class_dict: フィールドを記した辞書
        :return:    typeにより生成されたクラス定義
        """
        for key, value in class_dict.items():
            if isinstance(value, Attribute):
                value.name = key
                value.internal_name = '_{}'.format(key)

        # typeによりクラスを手動生成して返す
        cls = super(RowMeta, mcs).__new__(mcs, name, bases, class_dict)
        return cls


class AbstractRow(object):
    R"""
    メタクラスの適用先(__metaclass__のみ定義)
    """
    __metaclass__ = RowMeta


class SmartItem(AbstractRow):
    R"""
    商品の属性をここで定義
    """
    id = Attribute()
    name = Attribute()
    price = Attribute()
    stock = Attribute()


# クラスの使い方は特に変わらない
item = SmartItem()
print('Before: {}| {}'.format(repr(item.name), item.__dict__))

item.id = 'ITM001'
item.name = 'Grape'
item.price = 220
item.stock = 315
print('After: {}| {}'.format(repr(item.name), item.__dict__))
