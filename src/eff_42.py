# -*- coding: utf-8 -*-

R"""
デコレータを使用する
"""

from datetime import datetime
from functools import wraps


def sampling(func):
    R"""
    デコレート先関数を返す
    :param      func:   デコレート元関数
    :return:    デコレート先関数
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        R"""
        デコレート元関数の前後に時刻取得を行い、処理時間を表示する
        :param      args:   デコレート元関数へ渡す可変引数
        :param      kwargs: デコレート元関数へ渡すキーワード付き引数
        :return:    デコレート元関数の呼出結果
        """
        # 処理開始時刻取得
        start = datetime.now()

        # 測定したい本来の関数を呼び出す
        result = func(*args, **kwargs)

        # 処理終了時刻取得
        end = datetime.now()

        # 処理時間を表示
        print('所要時間 : {}'.format(end - start))

        # デコレート元関数の呼出結果を返す
        return result

    # 内部関数自体を返す
    return wrapper


def heavy_process(loop):
    for i in range(loop):
        pass


@sampling
def deco_heavy_process(loop):
    for i in range(loop):
        pass


# これらは等価
sampling(func=heavy_process)(loop=100000000)
deco_heavy_process(loop=100000000)
