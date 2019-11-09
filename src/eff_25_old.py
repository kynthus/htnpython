# -*- coding: utf-8 -*-

R"""
古い継承。今ではもう使われない
"""


class Base(object):
    R"""
    基底(親)クラス
    """

    def __init__(self, attr):
        self.attr = attr


class Derived(Base):
    R"""
    派生(子)クラス
    """

    def __init__(self, attr):
        # 古い基底クラスのコンストラクタ呼出
        Base.__init__(self, attr)
