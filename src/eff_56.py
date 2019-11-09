# -*- coding: utf-8 -*-

R"""
単体テスト用のコードを記述
"""

from unittest import TestCase, main


def str_to_int(string):
    R"""
    文字列を整数値へ変換する。
    :param      string:
    :return:    文字列を整数値へ変換した結果
    :raises     TypeError: 整数値以外の文字列が渡されたとき.
    """
    return int(string)


class StrToIntTest(TestCase):
    R"""
    str_to_int関数のテストクラス
    """

    def test_str_to_int_111(self):
        R"""
        文字列の'111'を指定した場合は、数値の111へ変換される。
        """
        self.assertEqual(first=111, second=str_to_int('111'))

    def test_str_to_int_bad_string(self):
        R"""
        数字文字列以外が指定した場合は、ValueErrorとなる。
        """
        self.assertRaises(ValueError, str_to_int, 'AAAA')

    def test_str_to_int_bad_type(self):
        R"""
        文字列以外のデータ型を指定した場合は、TypeErrorとなる。
        """
        self.assertRaises(TypeError, str_to_int, None)


# テストは必ずメインの時のみ実行させる
if __name__ == '__main__':
    main()
