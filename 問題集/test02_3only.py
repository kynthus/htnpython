# -*- coding: utf-8 -*-

R"""
Python問題集 その02
"""
import math
import numpy


def q01():
    R"""
    整数値を2つ入力し、それぞれの和差積商と余りを求めてください。
    """
    num1 = int(input('整数値1：'))
    num2 = int(input('整数値2：'))

    print('num1 + num2 = {:d}'.format(num1 + num2))
    print('num1 - num2 = {:d}'.format(num1 - num2))
    print('num1 * num2 = {:d}'.format(num1 * num2))
    print('num1 / num2 = {:f}'.format(num1 / num2))
    print('num1 % num2 = {:d}'.format(num1 % num2))


def q02():
    R"""
    3つの整数値を入力し、それらの合計と平均を求めてください。
    """
    num1 = int(input('整数値1：'))
    num2 = int(input('整数値2：'))
    num3 = int(input('整数値3：'))

    total = num1 + num2 + num3
    average = total / 3

    print('3つの整数値の合計：{:d}'.format(total))
    print('3つの整数値の平均：{:f}'.format(average))

    # 別解
    total2 = sum([num1, num2, num3])
    average2 = numpy.average([num1, num2, num3])

    print('3つの整数値の合計：{:d}'.format(total2))
    print('3つの整数値の平均：{:f}'.format(average2))


def q03():
    R"""
    入力された円の半径より、円周と面積を求めてください。
    """
    radius = float(input('半径：'))

    print('円周の長さ：{:f}'.format(2 * math.pi * radius))
    print('円の面積  ：{:f}'.format(math.pi * radius ** 2))


def q04():
    R"""
    2つの正の整数を入力し、後者が前者の約数かを判定してください。
    """
    num_A = int(input('整数A：'))
    num_B = int(input('整数B：'))

    if num_A % num_B == 0:
        print('BはAの約数である')
    else:
        print('BはAの約数ではない')


def q05():
    R"""
    2つの整数値の差を求めてください。
    """
    num1 = int(input('整数1：'))
    num2 = int(input('整数2：'))

    diff = num2 - num1 if num1 < num2 else num1 - num2
    print('2つの整数値の差は{:d}'.format(diff))


def q06():
    R"""
    入力した段数分、アスタリスク('*')のピラミッドを表示してください。
    """
    tier = int(input('段数：'))

    for i in range(tier):
        print(' ' * (tier - i - 1), end='')
        print('*' * (i * 2 + 1))


def q07():
    R"""
    キーボードから'q'が入力されるまで、入力文字列を表示し続けるプログラムを作成してください。
    """
    while True:
        line = input('文字列を入力：')

        if line == 'q':
            break

        print('入力された文字列[{}]'.format(line))


def q08():
    R"""
    2のn乗を求めて表示してください。
    """
    n = int(input('n：'))

    print('2^{:d} = {:d}'.format(n, 2 ** n))


def q09():
    R"""
    入力した数値が0-100の範囲であれば正当、範囲外の場合は不当と表示してください。
    """
    score = int(input('テストの点数：'))

    if 0 <= score <= 100:
        print('正当な点数')
    else:
        print('不当な点数')


def q10():
    R"""
    50未満のフィボナッチ数を表示してください。
    """
    lo = 1
    hi = 1

    print(lo)

    while hi < 50:
        print(hi)

        hi = lo + hi
        lo = hi - lo


if __name__ == '__main__':
    print('--- Q01 ---')
    q01()
    print('--- Q02 ---')
    q02()
    print('--- Q03 ---')
    q03()
    print('--- Q04 ---')
    q04()
    print('--- Q05 ---')
    q05()
    print('--- Q06 ---')
    q06()
    print('--- Q07 ---')
    q07()
    print('--- Q08 ---')
    q08()
    print('--- Q09 ---')
    q09()
    print('--- Q10 ---')
    q10()
