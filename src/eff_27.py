# -*- coding: utf-8 -*-

R"""
インポート除外メンバと非公開メンバ
"""


class Person(object):
    R"""
    メンバアクセスのテスト用
    """

    def __init__(self):
        R"""
        公開、除外対象、非公開の属性を定義
        """
        self.public_attr = 10
        self._protected_attr = 50
        self.__private_attr = 100

    def show(self):
        R"""
        全ての属性の値を表示する
        クラス内からは、いずれの属性もアクセス可能
        """
        print('public   : {}'.format(self.public_attr))
        print('protected: {}'.format(self._protected_attr))
        print('private  : {}'.format(self.__private_attr))


person = Person()

# 公開属性は何ら変わりなくアクセスできる
print(person.public_attr)

# インポート除外対象のメンバもアクセス可能(IntelliJは警告を出す)
# もしもimport *で引き込んだとき、_が1つ付いたメンバはインポートされない
print(person._protected_attr)

# 非公開メンバへはアクセスできない
# print(person.__private_attr)

# ……少し待たれい、こうすれば非公開メンバにもアクセス可能
# <インスタンス変数名>._<クラス名><非公開メンバ名>
print(person._Person__private_attr)
