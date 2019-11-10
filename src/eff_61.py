# -*- coding: utf-8 -*-

R"""
特殊メソッド
Python 2系は100種類, Python 3系は121種類
"""


class MyInteger(object):

    def __init__(self, integer):
        self.integer = integer

    # 左解決型算術演算子
    def __add__(self, other):
        print('__add__()')
        if isinstance(other, self.__class__):
            return self.__class__(self.integer + other.integer)
        elif isinstance(other, int):
            return self.__class__(self.integer + other)

    def __sub__(self, other):
        print('__sub__()')
        if isinstance(other, self.__class__):
            return self.__class__(self.integer - other.integer)
        elif isinstance(other, int):
            return self.__class__(self.integer - other)

    def __mul__(self, other):
        print('__mul__()')
        if isinstance(other, self.__class__):
            return self.__class__(self.integer * other.integer)
        elif isinstance(other, int):
            return self.__class__(self.integer * other)

    # Python 2系のみ
    def __div__(self, other):
        print('__div__()')
        if isinstance(other, self.__class__):
            return self.__class__(self.integer / other.integer)
        elif isinstance(other, int):
            return self.__class__(self.integer / other)

    def __mod__(self, other):
        print('__mod__()')
        if isinstance(other, self.__class__):
            return self.__class__(self.integer / other.integer)
        elif isinstance(other, int):
            return self.__class__(self.integer / other)

    def __pow__(self, power, modulo=None):
        print('__pow__()')
        if isinstance(power, self.__class__):
            return self.__class__(self.integer.__pow__(power.integer, modulo))
        elif isinstance(power, int):
            return self.__class__(self.integer.__pow__(power, modulo))

    # Python 2系では試験段階
    def __truediv__(self, other):
        print('__truediv__()')
        if isinstance(other, self.__class__):
            return self.__class__(self.integer / other.integer)
        elif isinstance(other, int):
            return self.__class__(self.integer / other)

    def __floordiv__(self, other):
        print('__floordiv__()')
        if isinstance(other, self.__class__):
            return self.__class__(self.integer // other.integer)
        elif isinstance(other, int):
            return self.__class__(self.integer // other)

    def __divmod__(self, other):
        print('__divmod__()')
        if isinstance(other, self.__class__):
            div, mod = divmod(self.integer, other.integer)
        elif isinstance(other, int):
            div, mod = divmod(self.integer, other)
        else:
            raise TypeError('Not integer type.')
        return self.__class__(div), self.__class__(mod)

    # 右解決型算術演算子
    def __radd__(self, other):
        print('__radd__()')
        if isinstance(other, self.__class__):
            return self.__class__(other.integer + self.integer)
        elif isinstance(other, int):
            return self.__class__(other + self.integer)

    def __rsub__(self, other):
        print('__rsub__()')
        if isinstance(other, self.__class__):
            return self.__class__(other.integer - self.integer)
        elif isinstance(other, int):
            return self.__class__(other - self.integer)

    def __rmul__(self, other):
        print('__rmul__()')
        if isinstance(other, self.__class__):
            return self.__class__(other.integer * self.integer)
        elif isinstance(other, int):
            return self.__class__(other * self.integer)

    # Python 2系のみ
    def __rdiv__(self, other):
        print('__rdiv__()')
        if isinstance(other, self.__class__):
            return self.__class__(other.integer / self.integer)
        elif isinstance(other, int):
            return self.__class__(other / self.integer)

    def __rmod__(self, other):
        print('__rmod__()')
        if isinstance(other, self.__class__):
            return self.__class__(other.integer % self.integer)
        elif isinstance(other, int):
            return self.__class__(other % self.integer)

    def __rpow__(self, power, modulo=None):
        print('__rpow__()')
        if isinstance(power, self.__class__):
            return self.__class__(self.integer.__rpow__(power.integer, modulo))
        elif isinstance(power, int):
            return self.__class__(self.integer.__rpow__(power, modulo))

    # Python 2系では試験段階
    def __rtruediv__(self, other):
        print('__rtruediv__()')
        if isinstance(other, self.__class__):
            return self.__class__(other.integer / self.integer)
        elif isinstance(other, int):
            return self.__class__(other / self.integer)

    def __rfloordiv__(self, other):
        print('__rfloordiv__()')
        if isinstance(other, self.__class__):
            return self.__class__(other.integer // self.integer)
        elif isinstance(other, int):
            return self.__class__(other // self.integer)

    def __rdivmod__(self, other):
        print('__divmod__()')
        if isinstance(other, self.__class__):
            div, mod = divmod(other.integer, self.integer)
        elif isinstance(other, int):
            div, mod = divmod(other, self.integer)
        else:
            raise TypeError('Not integer type.')
        return self.__class__(div), self.__class__(mod)

    # 複合代入算術演算子
    def __iadd__(self, other):
        print('__iadd__()')
        if isinstance(other, self.__class__):
            self.integer += other.integer
        elif isinstance(other, int):
            self.integer += other
        return self

    def __isub__(self, other):
        print('__isub__()')
        if isinstance(other, self.__class__):
            self.integer -= other.integer
        elif isinstance(other, int):
            self.integer -= other
        return self

    def __imul__(self, other):
        print('__imul__()')
        if isinstance(other, self.__class__):
            self.integer *= other.integer
        elif isinstance(other, int):
            self.integer *= other
        return self

    def __idiv__(self, other):
        print('__idiv__()')
        if isinstance(other, self.__class__):
            self.integer /= other.integer
        elif isinstance(other, int):
            self.integer /= other
        return self

    def __imod__(self, other):
        print('__imod__()')
        if isinstance(other, self.__class__):
            self.integer %= other.integer
        elif isinstance(other, int):
            self.integer %= other
        return self

    def __ipow__(self, other):
        print('__ipow__()')
        if isinstance(other, self.__class__):
            self.integer **= other.integer
        elif isinstance(other, int):
            self.integer **= other
        return self

    def __itruediv__(self, other):
        print('__itruediv__()')
        if isinstance(other, self.__class__):
            self.integer /= other.integer
        elif isinstance(other, int):
            self.integer /= other
        return self

    def __ifloordiv__(self, other):
        print('__ifloordiv__()')
        if isinstance(other, self.__class__):
            self.integer //= other.integer
        elif isinstance(other, int):
            self.integer //= other
        return self

    # 単項+/-演算子
    def __pos__(self):
        print('__pos__()')
        return self

    def __neg__(self):
        print('__neg__()')
        return self.__class__(-self.integer)

    # 比較演算子
    def __eq__(self, other):
        print('__eq__()')
        if isinstance(other, self.__class__):
            return self.integer == other.integer
        elif isinstance(other, int):
            return self.integer == other

    def __ne__(self, other):
        print('__ne__()')
        if isinstance(other, self.__class__):
            return self.integer != other.integer
        elif isinstance(other, int):
            return self.integer != other

    def __lt__(self, other):
        print('__lt__()')
        if isinstance(other, self.__class__):
            return self.integer < other.integer
        elif isinstance(other, int):
            return self.integer < other

    def __gt__(self, other):
        print('__gt__()')
        if isinstance(other, self.__class__):
            return self.integer > other.integer
        elif isinstance(other, int):
            return self.integer > other

    def __le__(self, other):
        print('__le__()')
        if isinstance(other, self.__class__):
            return self.integer <= other.integer
        elif isinstance(other, int):
            return self.integer <= other

    def __ge__(self, other):
        print('__ge__()')
        if isinstance(other, self.__class__):
            return self.integer >= other.integer
        elif isinstance(other, int):
            return self.integer >= other

    # Python 2系のみ。古い比較演算用
    def __cmp__(self, other):
        print('__cmp__()')
        if isinstance(other, self.__class__):
            integer = self.integer >= other.integer
        elif isinstance(other, int):
            integer = self.integer >= other
        else:
            raise TypeError('Not integer type.')
        if self.integer == integer:
            return 0
        elif self.integer < integer:
            return -1
        else:
            return 1

    # 左解決型ビット演算子
    def __and__(self, other):
        print('__and__()')
        if isinstance(other, self.__class__):
            return self.integer & other.integer
        elif isinstance(other, int):
            return self.integer & other

    def __or__(self, other):
        print('__or__()')
        if isinstance(other, self.__class__):
            return self.integer | other.integer
        elif isinstance(other, int):
            return self.integer | other

    def __xor__(self, other):
        print('__xor__()')
        if isinstance(other, self.__class__):
            return self.integer ^ other.integer
        elif isinstance(other, int):
            return self.integer ^ other

    def __lshift__(self, other):
        print('__lshift__()')
        if isinstance(other, self.__class__):
            return self.integer << other.integer
        elif isinstance(other, int):
            return self.integer << other

    def __rshift__(self, other):
        print('__rshift__()')
        if isinstance(other, self.__class__):
            return self.integer >> other.integer
        elif isinstance(other, int):
            return self.integer >> other

    # 右解決型ビット演算子
    def __rand__(self, other):
        print('__rand__()')
        if isinstance(other, self.__class__):
            return other.integer & self.integer
        elif isinstance(other, int):
            return other & self.integer

    def __ror__(self, other):
        print('__ror__()')
        if isinstance(other, self.__class__):
            return other.integer | self.integer
        elif isinstance(other, int):
            return other | self.integer

    def __rxor__(self, other):
        print('__rxor__()')
        if isinstance(other, self.__class__):
            return other.integer ^ self.integer
        elif isinstance(other, int):
            return other ^ self.integer

    def __rlshift__(self, other):
        print('__rlshift__()')
        if isinstance(other, self.__class__):
            return other.integer << self.integer
        elif isinstance(other, int):
            return other << self.integer

    def __rrshift__(self, other):
        print('__rrshift__()')
        if isinstance(other, self.__class__):
            return other.integer >> self.integer
        elif isinstance(other, int):
            return other >> self.integer

    # 複合代入ビット演算子
    def __iand__(self, other):
        print('__iand__()')
        if isinstance(other, self.__class__):
            self.integer &= other.integer
        elif isinstance(other, int):
            self.integer &= other
        return self

    def __ior__(self, other):
        print('__ior__()')
        if isinstance(other, self.__class__):
            self.integer |= other.integer
        elif isinstance(other, int):
            self.integer |= other
        return self

    def __ixor__(self, other):
        print('__ixor__()')
        if isinstance(other, self.__class__):
            self.integer ^= other.integer
        elif isinstance(other, int):
            self.integer ^= other
        return self

    def __ilshift__(self, other):
        print('__ilshift__()')
        if isinstance(other, self.__class__):
            self.integer <<= other.integer
        elif isinstance(other, int):
            self.integer <<= other
        return self

    def __irshift__(self, other):
        print('__irshift__()')
        if isinstance(other, self.__class__):
            self.integer >>= other.integer
        elif isinstance(other, int):
            self.integer >>= other
        return self

    # ビット反転
    def __invert__(self):
        print('__invert__()')
        return self.__class__(~self.integer)

    # 型変換関数用
    def __int__(self):
        print('__int__()')
        return self.integer

    # Python 2系のみ
    def __long__(self):
        print('__long__()')
        return int(self)

    def __float__(self):
        print('__float__()')
        return float(self.integer)

    def __str__(self):
        print('__str__()')
        return str(self.integer)

    # Python 2系のみ
    def __unicode__(self):
        print('__unicode__()')
        return str(self)

    # Python 3系のみ
    def __bytes__(self):
        print('__bytes__()')
        return bytes(str(self))


mint1 = MyInteger(100)

print(mint1 + 50)
print(mint1 - 50)
print(mint1 * 50)
print(mint1 / 50)
print(mint1 % 30)
print(mint1 ** 3)
print(mint1 // 50)
div1, mod1 = divmod(mint1, 50)
print('div:{}, mod:{}'.format(div1, mod1))

mint2 = MyInteger(5)

print(50 + mint2)
print(50 - mint2)
print(50 * mint2)
print(50 / mint2)
print(133 % mint2)
print(10 ** mint2)
print(53 // mint2)
div2, mod2 = divmod(8, mint2)
print('div:{}, mod:{}'.format(div2, mod2))

mint3 = MyInteger(0)
mint3 += 15
print(mint3)
mint3 -= 8
print(mint3)
mint3 *= 5
print(mint3)
mint3 /= 5
print(mint3)
mint3 %= 4
print(mint3)
mint3 **= 5
print(mint3)
mint3 //= 10
print(mint3)

print(+mint3)
print(-mint3)

mint4 = MyInteger(100)

print(mint4 == 100)
print(mint4 != 100)
print(mint4 < 100)
print(mint4 > 100)
print(mint4 <= 100)
print(mint4 >= 100)

# 比較演算子は左右なく、常にどちらの順でも呼び出せる
print(50 == mint4)
print(50 != mint4)
print(50 < mint4)
print(50 > mint4)
print(50 <= mint4)
print(50 >= mint4)

# ビット演算
print(mint4 & 0x55)
print(mint4 | 0x55)
print(mint4 ^ 0x55)
print(mint4 << 3)
print(mint4 >> 3)

mint5 = MyInteger(8)

print(0x55 & mint5)
print(0x55 | mint5)
print(0x55 ^ mint5)
print(0x55 << mint5)
print(0x55 >> mint5)

mint6 = MyInteger(0xFF)
mint6 &= 0x55
print(mint6)
mint6 |= 0x0F
print(mint6)
mint6 ^= 0xFF
print(mint6)
mint6 <<= 1
print(mint6)
mint6 >>= 1
print(mint6)

print(~mint6)

mint7 = MyInteger(500)
print(int(mint7))
print(float(mint7))
print(str(mint7))
print(bytes(mint7))
