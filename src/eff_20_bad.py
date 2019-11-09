# -*- coding: utf-8 -*-

R"""
デフォルト引数のワナ
"""


def get_list(data, default=[]):
    R"""
    引数とデフォルトのリストを連結した結果を返す(悪い例)
    :param      data:       末尾に連結するリスト
    :param      default:    デフォルトリスト
    :return:    連結したリスト
    """
    default += data

    return default


# 引数に渡したリストがそのまま返されると思いきや……
print(get_list(['A', 'B', 'C']))
print(get_list(['D', 'E', 'F']))
print(get_list(['G', 'H', 'Q']))
