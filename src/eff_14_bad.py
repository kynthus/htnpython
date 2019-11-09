# -*- coding: utf-8 -*-

R"""
Noneを使ったエラー処理
"""


def to_lower_case(msg):
    R"""
    英単語を大文字へ変換して返す
    空文字は空文字のまま、英文字以外を含む場合はNoneを返す
    :param      msg:    変換対象の文字列
    :return:    変換後の文字列
    """
    if msg == '' or msg.isalpha():
        return msg.upper()
    else:
        return None


# 「DUPLEX」を表示
r1 = to_lower_case('duplex')
if r1:
    print(r1)
else:
    print('msg is not alphabetic.')

# 「(空文字)」を表示(?)
r2 = to_lower_case('')
if r2:
    print(r2)
else:
    print('msg is not alphabetic.')

# エラー扱い
r3 = to_lower_case('12345')
if r3:
    print(r3)
else:
    print('msg is not alphabetic.')
