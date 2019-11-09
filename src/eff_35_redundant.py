# -*- coding: utf-8 -*-

R"""
クラス属性の注釈(冗長)
"""


class Attribute(object):
    R"""
    属性値を表す注釈用のクラス
    """

    def __init__(self, name):
        R"""
        属性値名を受け取り、外部用・内部用の双方を設定する
        :param  name:   属性値名
        """
        self.name = name
        self.internal_name = '_{}'.format(self.name)

    def __get__(self, instance, instance_type):
        R"""
        インスタンスよりディスクリプタを取得する
        :param      instance:       ディスクリプタを取得するインスタンス
        :param      instance_type:  ディスクリプタのデータ型
        :return:    取得したディスクリプタ
        """
        if not instance:
            return self

        return getattr(instance, self.internal_name, instance_type)

    def __set__(self, instance, value):
        R"""
        インスタンスに対してディスクリプタを設定する
        :param      instance:   設定対象のインスタンス
        :param      value:      設定する値
        """
        setattr(instance, self.internal_name, value)


class Item(object):
    R"""
    商品を表すクラス(各属性値への代入時に二回名前を指定するので冗長)
    """
    id = Attribute('id')
    name = Attribute('name')
    price = Attribute('price')
    stock = Attribute('stock')


# 最初は値が入っていない
item = Item()
print('Before: {}| {}'.format(repr(item.name), item.__dict__))

# 各属性値へ値を設定
item.id = 'ITM001'
item.name = 'Grape'
item.price = 220
item.stock = 315
print('After: {}| {}'.format(repr(item.name), item.__dict__))
