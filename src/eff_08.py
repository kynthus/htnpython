# -*- coding: utf-8 -*-

R"""
リスト内包表記
"""

nums = [1, 2, 3, 4, 5]

# SQLにおけるSELECT -> 変換
print([n + 10 for n in nums])  # [[11, 12, 13, 14, 15]
# 「map(lambda n: n + 10, nums)」と等価。こちらの方が速い

# SQLにおけるSELECT -> WHERE
print([n for n in nums if n % 2 == 0])  # [2, 4]
# 「filter(lambda n: n % 2 == 0, nums)」と等価。こちらの方が速い

# ifを書き連ねると複数条件を指定できる
print([n for n in nums if n % 2 == 0 if n < 3])  # [2]

# ORも可能
print([n for n in nums if n % 2 == 0 or n < 3])  # [1, 2, 4]

# SQLにおけるSELECT -> CASE
print([n if n % 2 == 0 else -n for n in nums])  # [-1, 2, -3, 4, -5]

# 二次元リストも簡単に作れる
print([[i, j] for i in range(5) for j in range(10)])  # [[0, 0], [0, 1], ... [4, 9]]

dim2 = [[i, j] for i in range(5) for j in range(10)]
# 二次元リストの平坦化
print([i for flat in dim2 for i in flat])  # [0, 0, 0, 1, ... 4, 9]

# あまり内包表記を乱用すると可読性が下がる
# 基準："for"と"if(else)"が合計3つ以上あると厳しい
print([
    (i if i < 5 else i * 2) + (j if j < 10 else -j)
    for i in range(10) if i % 2 != 0
    for j in range(20) if j % 2 == 0
])  # ↑……!?!?!?

# 分けましょう
odd10 = [i for i in range(10) if i % 2 != 0]
even20 = [j for j in range(20) if j % 2 == 0]
gt5dbl = [i if i < 5 else i * 2 for i in odd10]
gt10neg = [j if j < 10 else -j for j in even20]
print([i + j for i in gt5dbl for j in gt10neg])
