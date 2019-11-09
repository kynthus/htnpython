# -*- coding: utf-8 -*-

R"""
名前付きタプル(namedtuple)
"""

from collections import namedtuple

# 名前付きタプルを定義
City = namedtuple(
    'City',
    [
        'name',
        'country',
        'latitude',
        'longitude',
        'temperature',
        'elevation',
    ],  # []
)  # namedtuple

# コンストラクタと同様の形で呼び出せる
city = City(
    name='Philadelphia',
    country='USA',
    latitude=39.952,
    longitude=75.164,
    temperature=20,
    elevation=12,
)  # City

# 値の取得は属性アクセスで行える
print('name        = {}'.format(city.name))
print('country     = In {}'.format(city.country))
print('latitude    = {}'.format(city.latitude))
print('longitude   = {}'.format(city.longitude))
print('temperature = {}'.format(city.temperature))
print('elevation   = {}(m)'.format(city.elevation))
