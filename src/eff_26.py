# -*- coding: utf-8 -*-

R"""
ミックスイン(mix-in)
"""

from datetime import datetime, timedelta


class ShowMixin(object):
    R"""
    文字列変換を実装するミックスインクラス
    """

    def __str__(self):
        R"""
        クラス名とフィールド値を持つ文字列へ変換する
        :return:    クラスの文字列へ変換した結果
        """
        return '{}({})'.format(
            self.__class__.__name__,
            ','.join([str(v) for v in self.__dict__.values()])
        )  # format


class EqualMixin(object):
    R"""
    等価比較(==)を実装するミックスインクラス
    """

    def __eq__(self, other):
        R"""
        2つのインスタンスの属性辞書が一致するか否かを判定する
        :param      other:  別インスタンス
        :return:    属性辞書が一致する場合はTrue、一致しない場合はFalse
        """
        # otherがNoneの場合、そもそも一致しない
        if other is None:
            return False

        # たまたま属性辞書が同一の別クラスは、ちゃんと別モノとして扱う
        if type(self) != type(other):
            return False

        # 属性辞書を比較した結果を返す
        return self.__dict__ == other.__dict__


class Profile(ShowMixin, EqualMixin):
    R"""
    IDと氏名を保持するクラス
    """

    def __init__(self, ident, name):
        R"""
        IDと氏名で初期化する
        :param  ident:  ID
        :param  name:   氏名
        """
        self.ident = ident
        self.name = name


class TimeRange(ShowMixin, EqualMixin):
    R"""
    時刻の範囲を表すクラス
    """

    def __init__(self, start, end):
        R"""
        開始時刻と終了時刻で初期化する
        :param  start:  開始時刻
        :param  end:    終了時刻
        """
        self.start = start
        self.end = end


# プロフィール生成
kimura1 = Profile(ident='PR001', name='Kimura')
kimura2 = Profile(ident='PR001', name='Kimura')
yamamura = Profile(ident='PR001', name='Yamamura')

# ID, 氏名を文字列として表示
print(kimura1)
print(yamamura)

# kimura1とkimura2は同一、kimura1とyamamuraは同一ではない
print(kimura1 == kimura2)
print(kimura1 == yamamura)

# 時間範囲を生成
now = datetime.now()
until_tomorrow1 = TimeRange(start=now, end=now + timedelta(days=1))
until_tomorrow2 = TimeRange(start=now, end=now + timedelta(days=1))
since_yesterday = TimeRange(start=now - timedelta(days=1), end=now)

# 開始時刻, 終了時刻を文字列として表示
print(until_tomorrow1)
print(since_yesterday)

# until_tomorrow1, 2はどちらも「今から明日まで」で同一
# 一方でsince_yesterdayは「昨日から今まで」なので同一ではない
print(until_tomorrow1 == until_tomorrow2)
print(until_tomorrow1 == since_yesterday)
