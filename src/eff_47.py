# -*- coding: utf-8 -*-

R"""
Decimal型の使い方
"""

from decimal import Decimal

# 浮動小数点数は誤差が出る
floating_point = 1.62 + 0.41
print(floating_point)

# 10進型なら心配ない
decimal = Decimal(value='1.62') + Decimal(value='0.41')
print(decimal)
