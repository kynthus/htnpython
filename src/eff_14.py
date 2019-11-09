# -*- coding: utf-8 -*-

R"""
例外送出によるエラー処理
"""


def to_lower_case(msg):
    R"""
    英単語を大文字へ変換して返す
    空文字は空文字のまま、英文字以外を含む場合は例外として扱い
    :param      msg:    変換対象の文字列
    :return:    変換後の文字列
    :raises     ValueError: 引数の文字列が英文字以外だった場合
    """
    if msg == '' or msg.isalpha():
        return msg.upper()
    else:
        raise ValueError('msg is not alphabetic.')


# 「DUPLEX」を表示
try:
    print(to_lower_case('duplex'))
except ValueError as err:
    print(err)

# 「(空文字)」を表示
try:
    print(to_lower_case(''))
except ValueError as err:
    print(err)

# エラー扱い
try:
    print(to_lower_case('12345'))
except ValueError as err:
    print(err)
