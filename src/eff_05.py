# -*- coding: utf-8 -*-

R"""
リストのスライス
Pythonシェルでやりたいところだ
"""

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# 先頭4つを取得
print('First        4 : {}'.format(alpha[:4]))

# 末尾4つを取得
print('Last         4 : {}'.format(alpha[-4:]))

# 先頭4番目～末尾4番目までの範囲で取得
print('Range   4 to 5 : {}'.format(alpha[3:-3]))

# 元のリストのコピー
print('Copy       all : {}'.format(alpha[:]))

# さまざまなスライス方法
print('First        5 : {}'.format(alpha[:5]))
print('Exclude Last 1 : {}'.format(alpha[:-1]))
print('Last         4 : {}'.format(alpha[4:]))
print('Last         3 : {}'.format(alpha[-3:]))
print('Range   2 to 4 : {}'.format(alpha[2:5]))
print('Range   2 to 6 : {}'.format(alpha[2:-1]))
print('Range   5 to 6 : {}'.format(alpha[-3:-1]))

# 配列のインデックスを超えて指定も可能
print('Copy       all : {}'.format(alpha[:20]))
print('Copy       all : {}'.format(alpha[-20:]))

# スライスに代入すると、要素を置き換えることが可能
# 先頭3番目～7番目を除去し、代わりに[1,2,3]で置き換える
alpha[2:7] = [1, 2, 3]
print('Replace  1,2,3 : {}'.format(alpha))

# 配列の内容を丸ごと書き換える
alpha[:] = [100, 200, 300, 400, 500]
print('Update     all : {}'.format(alpha))
