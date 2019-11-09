# -*- coding: utf-8 -*-

R"""
ディスクリプタによる属性値の表現(※ただし共有)
"""


class Age(object):
    R"""
    寿命のディスクリプタを保持するクラス
    """

    def __init__(self):
        R"""
        デフォルト値(整数値の0)を生成する
        """
        self.__value = 0

    def __get__(self, *_):
        R"""
        年齢値を取得する
        引数は使用しないので受け棄て
        :return:    取得したディスクリプタ
        """
        return self.__value

    def __set__(self, _, value):
        R"""
        年齢値を設定する
        第二引数は使用しないので受け棄て
        :param  value:  設定するディスクリプタ
        """
        if not 0 <= value < 10000:
            raise ValueError('Age must be between 0 and 9999')

        self.__value = value


class AnimalLifespan(object):
    R"""
    犬・シロナガスクジラ・ガラパゴスゾウガメの寿命
    """
    Dog = Age()
    Blue_whale = Age()
    Galapagos_tortoise = Age()


# 一般的な動物の最短寿命
min_lifespan = AnimalLifespan()
min_lifespan.Dog = 10
min_lifespan.Blue_whale = 80
min_lifespan.Galapagos_tortoise = 100

# 一般的な動物の最長寿命
max_lifespan = AnimalLifespan()
max_lifespan.Dog = 13
max_lifespan.Blue_whale = 90
max_lifespan.Galapagos_tortoise = 152

# 最短・最長寿命を表示(最長寿命で上書きされてしまう)
print(min_lifespan.Dog)
print(max_lifespan.Dog)
print(min_lifespan.Blue_whale)
print(max_lifespan.Blue_whale)
print(min_lifespan.Galapagos_tortoise)
print(max_lifespan.Galapagos_tortoise)
