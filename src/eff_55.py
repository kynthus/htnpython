# -*- coding: utf-8 -*-

R"""
repr()によるデバッグ情報出力
★こいつはコード例を一気には見せず、小出しにする
"""

print('---- repr()なし ----')
print(100)
print('100')
print("100")

print('---- repr()あり ----')
print(repr(100))
print(repr('100'))
print(repr("100"))


class NGVector(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


ng_vec = NGVector(x=10.25, y=193.743, z=34.7292)

print(repr(ng_vec))


class MyVector(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return 'MyVector({}, {}, {})'.format(self.x, self.y, self.z)


my_vec = MyVector(x=10.25, y=193.743, z=34.7292)

print(repr(my_vec))
print(my_vec.__dict__)
