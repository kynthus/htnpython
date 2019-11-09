# -*- coding: utf-8 -*-

R"""
Python 2系ではizipを使う
注意事項として載せとくだけでいいか
"""

# 5教科の点数
import itertools

positive = xrange(100000000)
negative = reversed(xrange(-100000000, 0))

for p, n in itertools.izip(positive, negative):
    print('{} | {}'.format(p, n))
