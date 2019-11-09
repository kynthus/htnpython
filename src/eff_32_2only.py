# -*- coding: utf-8 -*-

R"""
遅延属性
★__getattr__でデフォルト値を取得
  __getattribute__で値取得のたびに独自処理入れる(DB妥当性の検証など)
  __setattr__で変更のたびにそれを知らせられる
  __delattr__で削除した際の処理も記述可能
"""


class CustomizableShop(object):
    R"""
    属性の読み書きの度に独自処理を入れる
    """

    def __init__(self, name, kind):
        R"""
        デフォルトでは店名と種類のみ持っている
        :param  name:   店名
        :param  kind:   店の種類
        """
        self.name = name
        self.kind = kind

    def __getattr__(self, item):
        R"""
        まだ定義されていない属性を、取得しようとした時に呼び出される
        既に定義されている場合は呼び出されない
        :param      item:   属性名
        :return:    たとえば属性のデフォルト値
        """
        print('__getattr__() called.')

        # 未定義の属性にはデフォルト値として-1を設定
        value = -1
        setattr(self, item, value)

        # デフォルト値を返す
        return value

    def __getattribute__(self, item):
        R"""
        属性を取得する度に呼び出される
        既に定義されているか否かは関係ない
        :param      item:   属性名
        :return:    定義済みの場合は設定されている属性値、未定義の場合はデフォルト値
        """
        print('__getattribute__() called.')

        # AttributeErrorの発生有無で未定義が否かを振り分け
        try:

            # 定義済みの場合は基底クラスの__getattribute__()で取得する
            return super(CustomizableShop, self).__getattribute__(item)

        except AttributeError:

            # 未定義場合は__getattr__()と同様
            value = -1
            setattr(self, item, value)

            # デフォルト値を返す
            return value

    def __setattr__(self, key, value):
        R"""
        属性に値を代入する際に呼び出される
        :param  key:    属性名
        :param  value:  属性に設定する値
        """
        print('__setattr()__ called.')

        # 基底クラスの__setattr__()で設定する
        super(CustomizableShop, self).__setattr__(key, value)

    def __delattr__(self, item):
        R"""
        属性をdelで削除した際に呼び出される
        :param      item:   属性名
        """
        print('__delattr()__ called.')

        # 基底クラスの__delattr__()で削除する
        super(CustomizableShop, self).__delattr__(item)


shop = CustomizableShop(
    "Knill's Farm Market",
    'Fruits and vegetables',
)  # CustomizableShop

print(shop.name)
print(shop.kind)
# print(hasattr(shop, 'place'))
shop.place = 100
print(shop.place)
del shop.place
print(shop.place)
