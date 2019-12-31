import time

import numba
import numpy


def bubble_sort(data):
    sorted_data = data.copy()

    for j in range(len(sorted_data), 0, -1):
        for i in range(j - 1):
            if sorted_data[i + 1] < sorted_data[i]:
                tmp = sorted_data[i]
                sorted_data[i] = sorted_data[i + 1]
                sorted_data[i + 1] = tmp
    
    return sorted_data


@numba.jit
def numba_bubble_sort(data):
    sorted_data = data.copy()

    for j in range(len(sorted_data), 0, -1):
        for i in range(j - 1):
            if sorted_data[i + 1] < sorted_data[i]:
                tmp = sorted_data[i]
                sorted_data[i] = sorted_data[i + 1]
                sorted_data[i + 1] = tmp

    return sorted_data


if __name__ == '__main__':
    src = numpy.array([2, 1, 8, 5, 4, 7, 9, 0, 6, 3])
    dst = numba_bubble_sort(src)
    print(src)
    print(dst)

    start = time.time()

    for i in range(1000000):
        numba_bubble_sort(src)

    end = time.time()

    print('time = {}(ms)'.format(end - start))

    start = time.time()

    for i in range(1000000):
        bubble_sort(src)

    end = time.time()

    print('time = {}(ms)'.format(end - start))
