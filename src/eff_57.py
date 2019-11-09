# -*- coding: utf-8 -*-

R"""
デバッグ用のテストプログラム
※なお、pdbはプロセスアタッチが原則不可能
"""


def binary_search(array, target):
    R"""
    標準ライブラリ使えば一発だが、デバッグ用に用意
    :param      array:  値を探索する配列
    :param      target: 探索対象の値
    :return:    探索対象の値を保持しているインデックス値。
                探索対象を複数保持する場合は、最初の位置を返す。
                見つからなかった場合はNoneを返す。
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid + 1
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return None


# 探索対象の配列
ary = [1, 7, 4, 2, 18]
# 探索する値
trg = 2

# 二分探索を行い、見つかった場合はインデックス値と共に表示する。
# 見つからなかった場合は「not found」と表示する。
found = binary_search(array=sorted(ary), target=trg)

if found:
    print('{} found at location {}'.format(trg, found))
else:
    print('{} not found.'.format(trg))
