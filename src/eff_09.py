# -*- coding: utf-8 -*-

R"""
ジェネレータ内包表記
"""

import os

# テキストを開く
with open('words.txt') as text_file:
    # 改行コードをLFにする
    # メモリ展開するよりも速く開始する
    line_lf = (line.rstrip(os.linesep) + '\n' for line in text_file.readlines())

    # 結果を表示
    for element in line_lf:
        print(element)
