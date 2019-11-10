# -*- coding: utf-8 -*-

R"""
引数持ちデコレータ
"""

# デコレートした関数の格納先となる辞書
show_top = {}


def func_register(*args, **kwargs):
    R"""
    登録関数をラップする
    :param      args:   デコレートする関数へ渡す可変長引数
    :param      kwargs: 辞書登録時に使用するキーワード付き引数
    :return:    デコレータ関数
    """

    def decorator(func):
        R"""
        デコレート対象の関数を辞書へ登録する
        :param  func:   デコレート対象となる関数
        """
        show_top[kwargs['event']] = lambda: func(*args)

    # 登録関数を返す
    return decorator


@func_register('内閣総理大臣', event='日本')
def japan(top):
    R"""
    日本の初代内閣総理大臣は伊藤博文
    :param  top:    元首名
    """
    print('初代{}:伊藤博文'.format(top))


@func_register('President', event='USA')
def america(top):
    R"""
    アメリカの初代大統領はジョージ・ワシントン
    :param  top:    元首名
    """
    print('First {}: George Washington'.format(top))


@func_register('King', event='Thailand')
def france(top):
    R"""
    タイ(現王朝)の初代国王はラーマ1世
    :param  top:    元首名
    """
    print('First {}: Rama I.'.format(top))


# キーで関数を取得する
show_top['日本']()
show_top['USA']()
show_top['Thailand']()
