# -*- coding: utf-8 -*-

R"""
組み込みのデータ構造・アルゴリズムを使う
"""

from collections import deque

# デックを使用。リストとの違いは、先頭への要素追加が速い
# リストは先頭への追加・削除がO(n)となる
# ScalaのListは末尾への追加・削除が遅い
# そもそもPythonのリストは配列なので、単純に語弊がある
# ただし、ランダムアクセス(添字指定)は先頭からなぞるため遅い
fifo = deque()
fifo.append(1)
x = fifo.popleft()
print(x)

# Python 3.7以前の辞書は順番が維持されなかった。
nd = {}
nd['id'] = 'CD001'
nd['name'] = 'Joseph'
nd['collect'] = 100
print(nd)

# Python 3.7以降も、互換性を持たせるためにこうしとく
from collections import OrderedDict

od = OrderedDict()
od['id'] = 'CD001'
od['name'] = 'Joseph'
od['collect'] = 100
print(od)

# デフォルト値を設定できる
# 通常の辞書だとKeyErrorだが、defaultdictならデフォルト値が返る
from collections import defaultdict

dd = defaultdict(lambda: 10000)
dd['metastore'] = 9083
print(dd['metastore'])
print(dd['server2'])

# 優先度付きキュー
# デキューする際は最小値から取り出される
from heapq import heappush, heappop

hq = []
heappush(hq, 5)
heappush(hq, 3)
heappush(hq, 7)
heappush(hq, 4)
print(heappop(hq))
print(heappop(hq))
print(heappop(hq))
print(heappop(hq))

# 二分探索を用いて高速に探索
'''
print(datetime.datetime.now())
big_list = list(range(200000000))
print(datetime.datetime.now())
print(big_list.index(190000000))
print(datetime.datetime.now())
print(bisect_left(big_list, 190000000))
print(datetime.datetime.now())
'''

# itertools
from itertools import *

chain('Hello', 'World')  # [H,e,l,l,o,W,o,r,l,d]
cycle('A')  # 無限に'A'が続く(遅延評価)
it1, it2, it3 = tee(range(100), 3)  # 指定した個数分のイテレータを取得する
# Python 2系は「izip_longest」
zip_longest([1, 2, 3], [4, 5, 6, 7, 8])  # 一番長いイテレータ分だけ用意され、足りない部分はNoneが入る

islice([1, 2, 3, 4, 5], 2, 4)  # [3,4] コピーは作成せず、イテレータを返す
takewhile(lambda n: n < 500, [1, 10, 100, 1000, 10000])  # 条件を満たすまで回るイテレータ
dropwhile(lambda n: n < 500, [1, 10, 100, 1000, 10000])  # 条件を満たさなくなったら回るイテレータ
# Python 2系は「ifilterfalse」
filterfalse(lambda n: n % 2 == 0, [1, 2, 3, 4, 5])  # 奇数のみ残す。filter()の逆

product('ABC', '123')  # [(A,1),(A,2),(A,3),(B,1),(B,2),(B,3),(C,1),(C,2),(C,3)]
permutations(['red', 'green', 'blue'])  # 繰り返しを許さない順列
combinations(['red', 'green', 'blue'], 2)  # 繰り返しを許さない組合せ
