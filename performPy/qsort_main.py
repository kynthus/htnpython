import pycqsort

import time


if __name__ == '__main__':
    src = [2, 1, 8, 5, 4, 7, 9, 0, 6, 3]
    dst = pycqsort.bubble_sort(src)
    print(src)
    print(dst)

    start = time.time()

    for i in range(1000000):
        pycqsort.bubble_sort(src)

    end = time.time()

    print('time = {}(ms)'.format(end - start))

    start = time.time()

    for i in range(1000000):
        bubble_sort(src)

    end = time.time()

    print('time = {}(ms)'.format(end - start))
