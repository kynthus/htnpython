# -*- coding: utf-8 -*-

R"""
Python 2系におけるキーワード専用引数
"""

# 果物リスト
FRUITS_LIST = [
    'Apple',
    'Orange',
    'Grape',
]  # []


def register(name, **kwargs):
    R"""
    果物をリストへ登録する
    :param  name:   新しく追加する果物の名前
    :param  kwargs: add_tailを持つキーワード付き引数
    """
    # 'add_tail'キーを取り出す
    add_tail = kwargs.pop('add_tail', False)
    # 'add_tail'以外のキーワードが存在した場合は例外として扱う
    if kwargs:
        raise TypeError('Unexpected **kwargs: {}'.format(kwargs))

    if add_tail:
        FRUITS_LIST.append(name)
    else:
        FRUITS_LIST.insert(0, name)


print(FRUITS_LIST)

# ヤシの実とイチゴは先頭、バナナは末尾へ追加
register('Palm')  # デフォルトでは先頭へ追加される
register('Strawberry', add_tail=False)  # キーワードの指定を強制できる
register('Banana', add_tail=True)

print(FRUITS_LIST)

# register('Strawberry', True) # キーワードなしでTrue,Falseと書くとエラー

# 誤ったキーワードも指定できてしまうので
# 関数側で例外として扱うなど対策が必要
register('ChiliPepper', add_head=True)
