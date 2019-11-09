# -*- coding: utf-8 -*-

R"""
ループ直後にelse(絶対やんない方がいい)
"""


def while_and_else(nums):
    R"""
    リストの全要素に100を足し合わせる
    ただし、負数が紛れている場合は途中で終了する
    :param  nums:   整数値のリスト
    """
    n = 0
    while n < len(nums):
        if nums[n] < 0:
            break
        nums[n] += 100
        n += 1
    else:
        print('All elements added 100.')


def for_and_else(message):
    R"""
    リストの全要素を文字列として連結する
    ただし、'q'が紛れている場合は途中で終了する
    :param  message:    整数値のリスト
    """
    combined = ''
    for n in message:
        if n == 'q':
            break
        combined += n
    else:
        print('All elements combined single string.')


# 「All elements added 100.」が表示される
while_and_else([1, 2, 3, 4, 5])
# 「All elements added 100.」は表示されない
while_and_else([1, 2, -1, -2, 0])

# 「All elements combined single string.」が表示される
for_and_else(['a', 'b', 'c', 'd', 'e'])
# 「All elements combined single string.」は表示されない
for_and_else(['o', 'p', 'q', 'r', 's'])
