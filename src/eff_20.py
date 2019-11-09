# -*- coding: utf-8 -*-

R"""
動的なデフォルト引数
"""


def get_list(data, default=None):
    R"""
    引数とデフォルトのリストを連結した結果を返す
    :param      data:       末尾に連結するリスト
    :param      default:    デフォルトリスト
                            引数が渡されなかった場合は空のリストとなる
    :return:    連結したリスト
    """
    if default is None:
        default = []

    default += data

    return default


# 引数に渡したリストがそのまま返される
print(get_list(['A', 'B', 'C']))
print(get_list(['D', 'E', 'F']))
print(get_list(['G', 'H', 'Q']))
