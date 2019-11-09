# -*- coding: utf-8 -*-

MODE = 'QA'
import sysprint

printer = sysprint.Printer('Hi!')
printer.show()
# ただし、これは開発・本番環境で変えるべき設定が1,2個など、
# 数が少ないケースでは有用だが、10個以上ある場合などは逆にややこしくなる。
# importを途中に挿んだり、__main__を使用するのはオススメしないので、
# 多くの変更が必要な場合は、いっそのこと設定ファイルに追い出す方がベター。
