# -*- coding: utf-8 -*-

R"""
循環依存問題について
"""

from mymodule.depA import dep_funcA
from mymodule.depB import dep_funcB

'''
depA.py -> depB.pyの順にインポートする
しかしdepB.pyもまた、depA.pyをインポートしに行く。
「depA.py -> depB.py -> depA.py」という依存関係が発生する。
よってdepA.pyを読み込むためにdepA.pyが必要となり、パラドックスに陥る。
Pythonでこのような循環依存が起こった場合、ImportErrorとなる。
'''
dep_funcA()
dep_funcB()
