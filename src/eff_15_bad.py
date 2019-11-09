# -*- coding: utf-8 -*-

R"""
nonlocalを使用しないとこうなる
"""


def linear_search(data, find):
    R"""
    クロージャ経由でリストから要素の線形探索を行う(悪い例)
    :param      data:   探索対象のリスト
    :param      find:   探索する要素
    :return:    ！！！実は常にFalseを返す！！！
    """
    found = False

    def inner_func():
        R"""
        検出フラグを一見すると書き換えそうなクロージャ関数
        """
        for d in data:
            if d == find:
                found = True

    # クロージャを呼び出してfoundフラグを更新(?)
    inner_func()

    return found


# Trueが返されるかと思いきや……
is_find = linear_search([1, 2, 3, 4, 5], 3)
print(is_find)
