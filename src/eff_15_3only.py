# -*- coding: utf-8 -*-

R"""
nonlocal修飾子
"""


def linear_search(data, find):
    R"""
    クロージャ経由でリストから要素の線形探索を行う
    :param      data:   探索対象のリスト
    :param      find:   探索する要素
    :return:    ！！！実は常にFalseを返す！！！
    """
    found = False

    def inner_func():
        R"""
        検出フラグを書き換えるクロージャ関数
        """
        for d in data:
            if d == find:
                # nonlocalを付けると外側のfound変数を使用する
                nonlocal
                found
                found = True

    # クロージャを呼び出してfoundフラグを更新
    inner_func()

    return found


# 今度はきちんとTrueが返される
is_find = linear_search([1, 2, 3, 4, 5], 3)
print(is_find)
