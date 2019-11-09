# -*- coding: utf-8 -*-

R"""
Python 3系のジェネレータ
"""

# Python 3系ではrange()でもジェネレータを生成する
gen = range(100000000)

# ただし、3系には逆にxrange()が存在しない
# そのため、後方互換性問題の1つといえる
# gen = xrange(100000000)

# ジェネレータ内包表記
minus_gen = (-x for x in gen)

# 負数に変換された値が表示される
for x in minus_gen:
    print(x)
