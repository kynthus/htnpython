# -*- coding: utf-8 -*-

R"""
辞書の問題
"""


def q01():
    R"""
    以下のような日本語と英単語が結び付いた2つのリストがあります。
    これらをループさせて和英翻訳結果を表示してください。
    """
    jplist = ['七面鳥', '白鳥', '紅鶴', '信天翁']
    enlist = ['Turkey', 'Swan', 'Flamingo', 'Albatross']

    for jp, en in zip(jplist, enlist):
        print('{} = {}'.format(jp, en))


def q02():
    R"""
    以下のようなリストがあります。
    このリストの何番目にどのような要素が存在するかを表示してください。
    """
    tastes = ['Peanuts', 'Strawberry', 'Caramel']

    for index, taste in enumerate(tastes):
        print('tastes[{:d}] = {}'.format(index, taste))


def q03():
    R"""
    以下のような辞書があります。この辞書の中身(キーと値)を表示してください。
    """
    dic = {'x': 10, 'y': 20, 'z': 30}

    for key, value in dic.items():
        print('dic[{}] = {:d}'.format(key, value))


def q04():
    R"""
    キーボードから入力した値までのキーを持ち、
    それぞれに累乗した値を紐付ける辞書を生成してください。
    """
    num = int(input('数値を入力：'))
    dic = {}

    for x in range(1, num + 1):
        dic[x] = x ** 2

    print(dic)


def q05():
    R"""
    以下の辞書から'y'を削除してください。
    """
    dic = {'x': 10, 'y': 20, 'z': 30}

    del dic['y']

    print(dic)


def q06():
    R"""
    2つのリストから辞書を生成してください。
    """
    keys = ['id', 'name', 'profession']
    values = ['HM001', 'David', 'Steel industry']

    dic = dict(zip(keys, values))

    print(dic)


def q07():
    R"""
    2つの辞書を連結してください。
    """
    dic1 = {'id': 'PR001', 'name': 'アリの巣コロリ'}
    dic2 = {'price': 413, 'category': '防虫剤'}

    dic1.update(dic2)

    print(dic1)


def q08():
    R"""
    以下のような辞書があります。
    この辞書にからキーを検索して値を表示してください。
    キーが存在しない場合は、その旨知らせてください。
    """
    dic = {'id': 'ST001', 'name': 'Steve', 'birthday': '1974-10-25'}

    key = input('キーを入力：')

    if key in dic:
        print('キー[{}]の値は[{}]'.format(key, dic[key]))
    else:
        print('キー[{}]は存在しない'.format(key))


def q09():
    R"""
    以下のような辞書があります。
    この辞書が'kind'と'price'があるかを調べてください。
    """
    dic = {'name': 'まだない', 'kind': 'ロシアンブルー', 'price': 150000}

    print(dic.keys() >= {'kind', 'price'})


def q10():
    R"""
    辞書のキーを大文字にした、新しい辞書を生成してください。
    """
    dic = {
        'shop_id': 'TK001',
        'shop_name': 'York Street Treat Inc',
        'address': 'Grayland St, Bonna 13'
    }

    print({key.upper(): value for key, value in dic.items()})


if __name__ == '__main__':
    print('--- Q01 ---')
    q01()
    print('--- Q02 ---')
    q02()
    print('--- Q03 ---')
    q03()
    print('--- Q04 ---')
    q04()
    print('--- Q05 ---')
    q05()
    print('--- Q06 ---')
    q06()
    print('--- Q07 ---')
    q07()
    print('--- Q08 ---')
    q08()
    print('--- Q09 ---')
    q09()
    print('--- Q10 ---')
    q10()
