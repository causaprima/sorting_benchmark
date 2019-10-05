import random


def bubble_sort(unsorted_array):
    a = unsorted_array.copy()
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


def selection_sort(unsorted_array):
    a = unsorted_array.copy()
    for i in range(len(a)-1):
        minimum = i
        for j in range(i + 1, len(a)):
            if a[j] < a[minimum]:
                minimum = j
        a[i], a[minimum] = a[minimum], a[i]
    return a


def insertion_sort(unsorted_array):
    a = unsorted_array.copy()
    for i in range(1, len(a)):
        j = i
        while a[j] < a[j-1] and j != 0:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
    return a


def cocktail_sort(unsorted_array):
    a = unsorted_array.copy()
    left = 0
    right = len(a) - 1
    while left <= right:
        for i in range(left, right, 1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
        right -= 1

        for j in range(right, left, -1):
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]
        left += 1
    return a


def merge_sort(unsorted_array):
    a = unsorted_array.copy()
    if len(a) <= 1:
        return a
    else:
        middle = len(a) // 2
        l = merge_sort(a[:middle])
        r = merge_sort(a[middle:])
        res = []
        i = j = 0
        while i < len(l) or j < len(r):
            if not i < len(l):
                res.append(r[j])
                j += 1
            elif not j < len(r):
                res.append(l[i])
                i += 1
            elif l[i] < r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        return res


def quick_sort(unsorted_array):
    a = unsorted_array.copy()
    if len(a) <= 1:
        return a
    else:
        pivot = random.choice(a)
    left_part = [n for n in a if n < pivot]
    middle_part = [pivot] * a.count(pivot)
    right_part = [n for n in a if n > pivot]
    return quick_sort(left_part) + middle_part + quick_sort(right_part)


def shell_sort(unsorted_array):
    a = unsorted_array.copy()
    inc = len(a) // 2
    while inc != 0:
        for i in range(inc, len(a), inc):
            j = i
            while a[j] < a[j-inc] and j != 0:
                a[j], a[j-inc] = a[j-inc], a[j]
                j -= inc
        inc = inc // 2
    return a


def heap_sort(unsorted_array):
    a = unsorted_array.copy()

    def heapify(a, n, i):
        top = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and a[i] < a[l]:
            top = l
        if r < n and a[top] < a[r]:
            top = r
        if top != i:
            a[i], a[top] = a[top], a[i]
            heapify(a, n, top)

    for i in range(len(a)-1, -1, -1):
        heapify(a, len(a), i)

    for i in range(len(a)-1, -1, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)

    return a