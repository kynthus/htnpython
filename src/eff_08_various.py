# -*- coding: utf-8 -*-

R"""
内包表記いろいろ
"""

# 集合内包表記
colors = {
    'Red', 'Green', 'Blue',
    'Cyan', 'Magenta', 'Yellow', 'Black'
}  # {}

# 全て小文字へ変換
print({e.lower() for e in colors})

# 辞書内包表記
pairs = {
    'id': 'BK001',
    'name': 'Linux in a nutshell',
    'price': 15,
}  # {}

# 全ての値に対して「Value : 」を付与
print({key: 'Value : {}'.format(pairs[key]) for key in pairs})

# items()でキーと値を一度に取得可能
print({
    'Key : {}'.format(key): 'Value : {}'.format(value)
    for key, value in pairs.items()
})  # print
