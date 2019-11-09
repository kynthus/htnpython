# -*- coding: utf-8 -*-

R"""
クロージャ
"""


def outer_func(outer_param):
    # 関数のなかで定義されたクロージャ関数
    def inner_func(inner_param):
        # クロージャから外側関数のスコープの変数へアクセス可能
        print('outer_param : {}'.format(outer_param))
        print('inner_param : {}'.format(inner_param))

    # クロージャを呼び出す
    inner_func(outer_param + 100)


outer_func(50)
