# -*- coding: utf-8 -*-

R"""
モジュールのドキュメント文字列
"""


def doc_func(arg):
    R"""
    関数のドキュメント文字列例
    :param      arg:    引数の説明
    :return:    戻り値の説明
    """
    print(arg)
    return 'arg is {}'.format(arg)


class DocClass(object):
    R"""
    クラスのドキュメント文字列
    """

    def method(self):
        R"""
        メソッドのドキュメント文字列
        """
        print('Method call.')
