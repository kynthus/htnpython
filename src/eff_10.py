# -*- coding: utf-8 -*-

R"""
リストの添字と値を一度に取得
"""

# 魚のリスト
fishes = ['Salmon', 'Flounder', 'Mackerel', 'Saury', 'Yellowtail']

# インデックスによるアクセス(避けたほうが良い)
for i in range(len(fishes)):
    print('fishes[{}] : {}'.format(i, fishes[i]))

# enumerate関数で添字に値を取得
for i, fish in enumerate(fishes):
    print('fishes[{}] : {}'.format(i, fish))
