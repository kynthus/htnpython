# -*- coding: utf-8 -*-

R"""
複数のリストを一度に回す
"""

# 5教科の点数
subjects = ['JAP', 'MAT', 'SOC', 'SCI', 'ENG']
scores = [75, 83, 35, 58, 80]

# インデックスによるアクセス(避けたほうが良い)
for i in range(5):
    print('{} : {}'.format(subjects[i], scores[i]))

# zip関数で2つのリストをまとめて回す
for subject, score in zip(subjects, scores):
    print('{} : {}'.format(subject, score))

# 2,3個ならまだいいが、規模が大きいデータであれば
# レコードとしてクラスにまとめよう
