# -*- coding: utf-8 -*-

R"""
Python 3系における文字列型
"""

import os

# こちらはstr型で、Unicodeとなる
# Python 2系と違い'u'を付けなくて良くなった
str_hello = 'hello'

# 'b'を付けるとbytes型となる
# ASCII形式となるので、全角文字は許容しない
unicode_hello = b'hello'

# それぞれのバイナリ表現を取得
print(list(str_hello))
print(list(unicode_hello))

# 内部表現が異なるため、str型とbytes型の比較は一致しない
# 実行時にUnicodeWarningも併せて発生する
if 'hello' == b'hello':
    print('These japanese phrases are same.')
else:
    # 必ずコッチ
    print('These japanese phrases are difference.')

# str型とbytes型は、例え空文字列でも別モノ扱い
if '' == b'':
    print('These empty strings are same.')
else:
    # 必ずコッチ
    print('These empty strings are difference.')

# ファイルへの書き込み
# Python 2系ではバイナリモードがデフォルトだったためバイト表現が許されたが、
# 3系ではアスキーモードのため、バイト配列の書き込みは許されない
'''
with open('japanese.txt', 'w') as text_file:
    text_file.write(os.urandom(10))
'''

# 3系でバイナリで書き込みたければ'wb'指定で開くように
with open('japanese.txt', 'wb') as text_file:
    text_file.write(os.urandom(10))
