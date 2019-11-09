# -*- coding: utf-8 -*-

R"""
ディスクリプタによる属性値の表現
★@propertyと@attr.setterの爆発を防止する
"""

from weakref import WeakKeyDictionary


class Age(object):
    R"""
    寿命を表すディスクリプタクラス
    """

    def __init__(self):
        R"""
        弱参照辞書を生成する
        他のインスタンスが手放した瞬間に解放される
        """
        self.__values = WeakKeyDictionary()

    def __get__(self, instance, _):
        R"""
        年齢値が存在する場合は年齢値を取得し、存在しない場合はデフォルト年齢(0)を返す
        第三引数は使用しないので受け棄て
        :param      instance:   年齢値の取得元インスタンス
        :return:    インスタンスが持つ年齢値
        """
        if instance is None:
            return self

        # 弱参照辞書よりインスタンスに対応するディスクリプタを返す
        return self.__values.get(instance, 0)

    def __set__(self, instance, value):
        R"""
        インスタンスに対して年齢値を設定する
        :param      instance:   年齢値の設定先インスタンス
        :param      value:      設定する年齢値
        """
        if not 0 <= value < 10000:
            raise ValueError('Age must be between 0 and 9999')

        # 弱参照辞書中のインスタンスに対応するディスクリプタへ設定する
        self.__values[instance] = value


class AnimalLifespan(object):
    R"""
    犬・シロナガスクジラ・ガラパゴスゾウガメの寿命
    """
    Dog = Age()
    Blue_whale = Age()
    Galapagos_tortoise = Age()


# 短くて平均どれほど生きるか
min_lifespan = AnimalLifespan()
min_lifespan.Dog = 10
min_lifespan.Blue_whale = 80
min_lifespan.Galapagos_tortoise = 100

# 長くて平均どれほど生きるか
max_lifespan = AnimalLifespan()
max_lifespan.Dog = 13
max_lifespan.Blue_whale = 90
max_lifespan.Galapagos_tortoise = 152

# 最短・最長寿命を表示
print(min_lifespan.Dog)
print(max_lifespan.Dog)
print(min_lifespan.Blue_whale)
print(max_lifespan.Blue_whale)
print(min_lifespan.Galapagos_tortoise)
print(max_lifespan.Galapagos_tortoise)
