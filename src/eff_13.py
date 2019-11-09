# -*- coding: utf-8 -*-

R"""
例外処理
"""


def divide(value1, value2):
    R"""
    0除算を検出できる関数
    :param      value1: 被除数
    :param      value2: 除数
    :return:    除算結果
    """
    try:
        # 例外が発生する可能性のある処理
        result = value1 / value2
    except ZeroDivisionError:
        # ZeroDivisionErrorが発生した時に走る
        print('divide in zero.')
    else:
        # 正常に処理が完了するか、
        # ZeroDivisionError以外の例外が発生した時に走る
        print(result)
    finally:
        # 最後に必ず走る
        print('Function return.')


# 2.0
divide(100, 50)

# 0.0
divide(0, 30)

# divide in zero.
divide(172, 0)

# TypeErrorが発生する
divide('888', 111)
