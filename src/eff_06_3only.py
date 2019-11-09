# -*- coding: utf-8 -*-

R"""
スライスにおけるstride指定
"""

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# スライスでは3つ目の指定が可能
print(alpha[::2])
print(alpha[1::2])

# start, endとの併用
print(alpha[2::2])
print(alpha[-2::-2])
print(alpha[-2:2:-2])
print(alpha[2:2:-2])

# 先頭から3, 5, 7番目に対し、それぞれ1, 2, 3を設定
alpha[2::2] = [1, 2, 3]
print(alpha)
# 実に分かりづらい……

# リストを逆順にする
print(alpha[::-1])

# マルチバイト文字はUnicodeなら逆順にできる
print('シマウマ'[::-1])

# Python 2のUTF-8やエンコードしたバイト列は不可能
utf_okapi = 'オカピ'.encode('UTF-8')
print(utf_okapi[::-1])

# スライスの3番目、stride指定はできる限り使うのは避けたい
# 使う際は必ずコメントにどのようなリストを返すか残すこと
# リスト反転はreversed()とlist()でも可能
print(list(reversed(alpha)))


'''
1000万回繰り返して測定
若干stride反転の方が速い
time = 2.255128860473633
time = 2.652151584625244
time = 2.414138078689575
time = 2.722155809402466
'''
