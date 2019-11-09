# -*- coding: utf-8 -*-

R"""
ジェネレータ内包表記(非効率)
"""

import os

# テキストを開く
with open('words.txt') as text_file:
    # 改行コードをLFにする
    # 全行をメモリへ展開するので、ファイルサイズ次第ではメモリ不足
    line_lf = [line.rstrip(os.linesep) + '\n' for line in text_file.readlines()]

    # 結果を表示
    for element in line_lf:
        print(element)
