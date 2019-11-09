# -*- coding: utf-8 -*-

R"""
可変長引数
"""


def hellos(*args):
    R"""
    引数に受け取った人物に挨拶する関数
    :param  args:   挨拶する人達
    """
    if args:
        print('Hello', end='')

        # 可変長引数から、forでそれぞれ名前を取得可能
        for name in args:
            print(', {}'.format(name), end='')
        print()

    else:
        print("I'm lonely...")


# 引数をいくらでも指定できる
hellos('Bob', 'Mark', 'Kerry')
hellos()

# リストを'*'を付けると展開して送られる
names = ['Anna', 'Ed', 'Simon']
hellos(*names)
