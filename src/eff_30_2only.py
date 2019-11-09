# -*- coding: utf-8 -*-

R"""
プロパティとセッタ
★継承と組み合わせるとコンストラクタ値も検査可能
"""


class AbstractPerson(object):
    R"""
    個人情報の抽象クラス
    """

    def __init__(self, ident, name, age):
        R"""
         ID・氏名・年齢をもとに個人情報を生成
         :param  ident:  ID
         :param  name:   氏名
         :param  age:    年齢
         """
        self.ident = ident
        self.name = name
        self.age = age


class Person(AbstractPerson):
    R"""
    簡単な個人情報(ID・氏名・年齢)
    """

    def __init__(self, ident, name, age):
        R"""
        ID・氏名・年齢をもとに個人情報を生成
        :param  ident:  ID
        :param  name:   氏名
        :param  age:    年齢
        """
        super(Person, self).__init__(ident, name, age)
        self.__ident = ident
        self.__name = name
        self.__age = age

    @property
    def ident(self):
        R"""
        IDを取得するプロパティ
        :return:    ID
        """
        return self.__ident

    @ident.setter
    def ident(self, ident):
        R"""
        IDを設定するセッタ
        :param  ident:  ID
        """
        if not ident:
            raise ValueError('ID is necessary.')
        self.__ident = ident

    @property
    def name(self):
        R"""
        氏名を取得するプロパティ
        :return:    氏名
        """
        return self.__name

    @name.setter
    def name(self, name):
        R"""
        氏名を設定するセッタ
        :param  name:   氏名
        """
        if not name:
            raise ValueError('Name is necessary.')
        self.__name = name

    @property
    def age(self):
        R"""
        年齢を取得するプロパティ
        :return:    年齢
        """
        return self.__age

    @age.setter
    def age(self, age):
        R"""
        年齢を設定するセッタ
        公開したくない場合はNoneでも良いが、公開する場合は0～150歳の間でなければならない
        :param  age:    年齢
        """
        if not 0 <= age <= 150:
            raise ValueError('Age must between 0 and 150.')
        self.__age = age

    @property
    def profile(self):
        R"""
        プロフィールを取得するプロパティ
        :return:    プロフィールを取得するプロパティ
        """
        return 'name:{} age:{}'.format(self.name, self.age)


# 個人情報生成
person = Person(
    ident='HM001',
    name='Ludolf Treu',
    age=58,
)

# プロパティであれば、()なしでアクセスできる
print(person.age)

# セッタが定義されていれば、代入可能
person.age = 18
print(person.age)

# 属性値以外をプロパティにすることも可能
print(person.profile)
