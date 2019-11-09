# -*- coding: utf-8 -*-

R"""
引数のキーワード指定
"""


def height(amount, unit='cm'):
    return '{}({})'.format(amount, unit)


def weight(amount, unit='kg'):
    return '{}({})'.format(amount, unit)


# 身長と体重が、それぞれデフォルトの単位で表示される
print('height : {}'.format(height(171.8)))
print('weight : {}'.format(weight(65.3)))

# 第2引数で単位を指定できるが、それが単位だとは少々分かりづらい
print('height : {}'.format(height(200, 'mm')))
print('weight : {}'.format(weight(118, 'g')))

# キーワード引数として'unit'と書けば、単位を指定したと一目で分かる
print('height : {}'.format(height(15, unit='m')))
print('weight : {}'.format(weight(30, unit='t')))
