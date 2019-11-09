# -*- coding: utf-8 -*-

R"""
例外クラスを自作する
"""


class MyException(Exception):
    R"""
    オリジナルのルート例外
    """


class InvalidArgumentError(MyException):
    R"""
    引数不正を示すエラー
    """


def func(arg1, arg2):
    R"""
    2つの自然数を連結する関数
    :param      arg1:   自然数1
    :param      arg2:   自然数2
    :return:    arg1とarg2を" : "でつなげた文字列
    """
    if arg1 < 0 or arg2 < 0:
        raise InvalidArgumentError(R'Negative number not allowed.')

    return '{} : {}'.format(arg1, arg2)


try:
    func(10, 25)
    func(768, 1584)
    # この負数による例外はAPIの使い方が間違っているため
    # 自作の例外クラスで捕捉する
    func(999, -1)
except InvalidArgumentError as err:
    print(err)
except MyException as err:
    print(R'Argument is normality...')
    print(err)
# もしも捕捉できない例外が発生した場合、APIのバグだと断定できる
# 内部処理でのデータ型が合っていなかったりなど
