# -*- coding: utf-8 -*-

R"""
三項式(条件演算子)
"""


# if - elseの条件判定を用いる
def my_abs(num):
    if num < 0:
        return -num
    else:
        return num


# 3項式を使えば1行で済む
def my_abs2(num):
    return -num if num < 0 else num


print(my_abs(5))
print(my_abs(-5))
print(my_abs(0))

print(my_abs2(5))
print(my_abs2(-5))
print(my_abs2(0))
