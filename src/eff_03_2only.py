# -*- coding: utf-8 -*-

R"""
Python 2系における文字列型
"""

import os

# こちらはstr型で、UTF-8となる
# 厳密にはソースの1行目にある「coding」に指定したもの
str_hello = 'こんにちは'

# 'u'を付けるとunicode型となり
# 文字通りUnicodeで扱われる
unicode_hello = u'こんにちは'

# それぞれのバイナリ表現を取得
print(list(str_hello))
print(list(unicode_hello))

# 内部表現が異なるため、str型とunicode型の比較は一致しない
# 実行時にUnicodeWarningも併せて発生する
if 'いろはにほへと' == u'いろはにほへと':
    print('These japanese phrases are same.')
else:
    # 必ずコッチ
    print('These japanese phrases are difference.')

# ただし、空文字列の場合は同一と判断される
if '' == u'':
    print('These empty strings are same.')
else:
    print('These empty strings are difference.')

# ファイルへの書き込み
# Python 2系ではデフォルトでバイナリモードで開くため
# byte表現を書き込むことが可能
with open('japanese.txt', 'w') as text_file:
    text_file.write(os.urandom(10))
