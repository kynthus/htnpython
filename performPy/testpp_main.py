import time

import pycpptest


if __name__ == '__main__':
    pycpptest.prog01_01()
    pycpptest.prog01_02()
    pycpptest.prog01_03()
    print(pycpptest.prog01_04(400, 150))
    print(pycpptest.prog01_05(100, 200))
    print(pycpptest.prog01_05(augend=111, addend=222))
