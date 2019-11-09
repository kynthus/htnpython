# -*- coding: utf-8 -*-

import sys

if sys.platform.startswith('win32'):
    print('Windows')
elif sys.platform.startswith('darwin'):
    print('Mac OS')
elif sys.platform.startswith('linux'):
    print('Linux')
elif sys.platform.startswith('aix'):
    print('AIX')
elif sys.platform.startswith('cygwin'):
    print('Win/Cygwin')
else:
    print('Unknown OS')
