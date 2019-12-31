import numpy

import pycppnumpy

if __name__ == '__main__':
    array = numpy.array([2.42, 3.78, 5.94, 1.08, 4.32])
    print('--- 乗算前 ---')
    print(array)

    multed = pycppnumpy.mult_array(array=array, scalar=5.0)
    print('--- 乗算後 ---')
    print(multed)
