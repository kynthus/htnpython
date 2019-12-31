def bubble_sort(list data):
    cdef int i
    cdef int j

    sorted_data = data[:]

    for j in range(len(sorted_data), 0, -1):
        for i in range(j - 1):
            if sorted_data[i + 1] < sorted_data[i]:
                tmp = sorted_data[i]
                sorted_data[i] = sorted_data[i + 1]
                sorted_data[i + 1] = tmp

    return sorted_data

def quick_sort(list data, int left, int right):
    cdef int tmp
    cdef int i = left
    cdef int j = right
    cdef int pivot = data[(left + right) // 2]

    while True:
        while data[i] < pivot:
            i += 1
        while pivot < data[j]:
            j -= 1

        if j <= i:
            break

        tmp = data[i]
        data[i] = data[j]
        data[j] = tmp

        i += 1
        j -= 1

    if left < i - 1:
        quick_sort(data, left, i - 1)
    if j + 1 < right:
        quick_sort(data, j + 1, right)
