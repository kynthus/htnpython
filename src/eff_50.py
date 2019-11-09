# -*- coding: utf-8 -*-

R"""
自作モジュールを使用する
"""

# 通常のインポート文
import mymodule.prints
# asを使って別名を付ける
import mymodule.prints as mp
# fromを使ってモジュール名でアクセス可能に
from mymodule import prints

mymodule.prints.hello1()
mp.hello2()
prints.hello3()

# *でモジュール以下全てを引き込む
import mymodule.calcs

print(mymodule.calcs.add(augend=10, addend=5))
print(mymodule.calcs.subtract(minuend=10, subtrahend=5))
# print(multiply(multiplier=10, multiplicand=5))
print(mymodule.calcs.divide(dividend=10, divisor=5))
print(mymodule.calcs.hello(value=777))

# 複数モジュールで同名の機能がある場合は別名を付ける
from mymodule.prints import hello as p_hello

p_hello()
