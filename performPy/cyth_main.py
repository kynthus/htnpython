import cythonlist

import time


def bubble_sort(data):
    sorted_data = data[:]

    for j in range(len(sorted_data), 0, -1):
        for i in range(j - 1):
            if sorted_data[i + 1] < sorted_data[i]:
                tmp = sorted_data[i]
                sorted_data[i] = sorted_data[i + 1]
                sorted_data[i + 1] = tmp

    return sorted_data


if __name__ == '__main__':
    src = [2, 1, 8, 5, 4, 7, 9, 0, 6, 3]
    dst = cythonlist.bubble_sort(src)
    print(src)
    print(dst)

    start = time.time()

    for i in range(1000000):
        cythonlist.bubble_sort(src)

    end = time.time()

    print('time = {}(ms)'.format(end - start))

    start = time.time()

    for i in range(1000000):
        bubble_sort(src)

    end = time.time()

    print('time = {}(ms)'.format(end - start))
