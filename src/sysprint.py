# -*- coding: utf-8 -*-


import __main__


class DevelopmentPrinter(object):
    def __init__(self, msg):
        self.msg = msg

    def show(self):
        print('Dev:' + self.msg)


class QAPrinter(object):
    def __init__(self, msg):
        self.msg = msg

    def show(self):
        print('QA:' + self.msg)


class ProductPrinter(object):
    def __init__(self, msg):
        self.msg = msg

    def show(self):
        print('Pro:' + self.msg)


if __main__.MODE == 'Dev':
    Printer = DevelopmentPrinter
elif __main__.MODE == 'QA':
    Printer = QAPrinter
else:
    Printer = ProductPrinter
