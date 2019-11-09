# -*- coding: utf-8 -*-

R"""
数値計算用の関数群
"""

# これを指定すると提供する機能を限定できる
# importで全指定なら持ってこれてしまう
# でも正直、あまり使わないほうがいいと思う
__all__ = ['add', 'subtract']


def add(augend, addend):
    return augend + addend


def subtract(minuend, subtrahend):
    return minuend - subtrahend


def multiply(multiplier, multiplicand):
    return multiplier * multiplicand


def divide(dividend, divisor):
    return dividend / divisor


def hello(value):
    return 'Hello, {}.'.format(value)
