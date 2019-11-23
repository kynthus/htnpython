# -*- coding: utf-8 -*-

R"""
Python問題集 その01
"""
import os


def q01():
    R"""
    コンソール画面へ自分の氏名を表示してください。
    """
    print('秦野 友輔')


def q02():
    R"""
    自分の性と名を、文字列連結して表示してください。
    """
    print('秦野' + ' ' + '友輔')


def q03():
    R"""
    自分の氏名を、一旦変数に入れてから表示してください。
    """
    msg = '秦野 友輔'

    print(msg)


def q04():
    R"""
    末尾を改行せずに自分の氏名を表示してください。
    """
    print('秦野 友輔', end='')


def q05():
    R"""
    コンソール画面上で文字列を入力して、それを表示してください。
    """
    input_word = input('キーボードから何か入力しなさい：')

    print('入力した内容：[' + input_word + ']')


def q06():
    R"""
    1回のprint()で、複数行の文字列を表示させてください。
    """
    msg = 'こんにちは！' + os.linesep + '元気ですかッ！？'

    print(msg)


def q07():
    R"""
    文字列連結を使用せずに、
    自分の性と名を1回のprint()で横並びに表示してください。
    """
    print('秦野', '友輔')


def q08():
    R"""
    無印のPythonコマンドでプログラムを実行し、
    末尾を改行せずに自分の氏名を表示してください。
    """
    print('秦野 友輔', end='')


def q09():
    R"""
    3つの文字列を入力し、それぞれの内容を表示してください。
    無印のpythonコマンドで実行すること。
    """
    input1 = input('文字列その1：')
    input2 = input('文字列その2：')
    input3 = input('文字列その3：')

    print('文字列その1は[' + input1 + ']')
    print('文字列その2は[' + input2 + ']')
    print('文字列その3は[' + input3 + ']')


def q10():
    R"""
    5人分の名前を入力して、それらを横並びで表示してください。
    ただし、文字列連結を使用してはいけません。
    無印のpythonコマンドで実行すること。
    """
    input1 = input('1人目：')
    input2 = input('2人目：')
    input3 = input('3人目：')
    input4 = input('4人目：')
    input5 = input('5人目：')

    print(input1, input2, input3, input4, input5)


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
