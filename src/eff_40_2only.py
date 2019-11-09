# -*- coding: utf-8 -*-

R"""
コルーチンによる並行処理
"""


def name_generator():
    R"""
    兄弟の名前を返すコルーチン
    :return:    兄弟の名前(年齢順)
    """
    yield 'Taro'
    yield 'Jiro'
    yield 'Saburo'
    yield 'Shiro'
    yield 'Alexander, Jr'
    yield 'Goro'


# コルーチンからの結果はnext()で順に取得できる
names = name_generator()
print(next(names))
print(next(names))
print(next(names))
print(next(names))
print(next(names))
print(next(names))


def loop_generator():
    R"""
    1から10までの数値を返すコルーチン
    :return:    1から10までの数値
    """
    for i in (i + 1 for i in range(10)):
        print('Please speak {}'.format(i))
        # ループの度に呼出元へ戻る
        yield i
        # 再度コルーチンへ入ってきた際は、yieldの直後から始まる
        print('Well done.')


# for文でコルーチンを呼び出すことも可能
for num in loop_generator():
    # yield式の直後はこちらへ戻る
    print('OK, {}!'.format(num))
    # ループが1回終了する毎に再度コルーチンへ入りなおす


def from_generator(n):
    R"""
    1からnまでの奇数を返すコルーチン
    ※Python 2系はムリ。大人しくforで返そう
    :param      n:  上限値(含まれる)
    :return:    1からnまでの奇数
    """
    for j in (i for i in xrange(1, n + 1) if i % 2 != 0):
        yield j


# 1から15までの奇数を取得
print(','.join((str(i) for i in from_generator(n=15))))
