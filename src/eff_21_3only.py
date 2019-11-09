# -*- coding: utf-8 -*-

R"""
キーワード専用引数
"""

# 果物リスト
FRUITS_LIST = [
    'Apple',
    'Orange',
    'Grape',
]  # []


def register(name, *, add_tail=False):
    R"""
    果物をリストへ登録する
    :param  name:       新しく追加する果物の名前
    :param  add_tail:   Trueの場合は末尾へ追加される
    """
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
