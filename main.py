from sorting_algorithms import *
import random
import timeit
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

array = pd.DataFrame(
    index=['bubble_sort', 'selection_sort', 'insertion_sort', 'cocktail_sort',
           'merge_sort', 'quick_sort', 'shell_sort', 'heap_sort'],
    columns=[100, 500, 1000, 5000, 10000],
    dtype=float
)

for j in array.columns:
    a = [random.randint(0, int(j)) for i in range(int(j))]
    for i in array.index:
        stmt = '{}(a)'.format(i)
        setp = 'from __main__ import a, {}'.format(i)
        print('processing [{}]\tarray size: {}'.format(i, j), end='')
        array.at[i, j] = timeit.timeit(stmt, setp, number=1)
        print('\t\ttiming:\t{}'.format(array.at[i, j]))
array.to_csv(r'/Users/home/PycharmProjects/Theory_of_computation/array.csv', sep=',')
print(array)


ascending_array = pd.DataFrame(
    index=['bubble_sort', 'selection_sort', 'insertion_sort', 'cocktail_sort',
           'merge_sort', 'quick_sort', 'shell_sort', 'heap_sort'],
    columns=[100, 500, 1000, 5000, 10000],
    dtype=float
)

for j in ascending_array.columns:
    a = sorted([random.randint(0, int(j)) for i in range(int(j))])
    for i in ascending_array.index:
        stmt = '{}(a)'.format(i)
        setp = 'from __main__ import a, {}'.format(i)
        print('processing [{}]\tascending_array size: {}'.format(i, j), end='')
        ascending_array.at[i, j] = timeit.timeit(stmt, setp, number=1)
        print('\t\ttiming:\t{}'.format(ascending_array.at[i, j]))
ascending_array.to_csv(r'/Users/home/PycharmProjects/Theory_of_computation/ascending_array.csv', sep=',')
print(ascending_array)


descending_array = pd.DataFrame(
    index=['bubble_sort', 'selection_sort', 'insertion_sort', 'cocktail_sort',
           'merge_sort', 'quick_sort', 'shell_sort', 'heap_sort'],
    columns=[100, 500, 1000, 5000, 10000],
    dtype=float
)

for j in descending_array.columns:
    a = sorted([random.randint(0, int(j)) for i in range(int(j))])[::-1]
    for i in descending_array.index:
        stmt = '{}(a)'.format(i)
        setp = 'from __main__ import a, {}'.format(i)
        print('processing [{}]\tdescending_array size: {}'.format(i, j), end='')
        descending_array.at[i, j] = timeit.timeit(stmt, setp, number=1)
        print('\t\ttiming:\t{}'.format(descending_array.at[i, j]))
descending_array.to_csv(r'/Users/home/PycharmProjects/Theory_of_computation/descending_array.csv', sep=',')
print(descending_array)

plt.figure()
plot = array.T.plot(logy=True, style='-o', figsize=(10, 8), xlim=[10, 11000])
plot.set_xlabel('array size')
plot.set_ylabel('time (sec)')
plt.savefig('/Users/home/PycharmProjects/Theory_of_computation/array.png')

plt.figure()
plot = ascending_array.T.plot(logy=True, style='-o', figsize=(10, 8), xlim=[10, 11000])
plot.set_xlabel('ascending_array size')
plot.set_ylabel('time (sec)')
plt.savefig('/Users/home/PycharmProjects/Theory_of_computation/ascending_array.png')

plt.figure()
plot = descending_array.T.plot(logy=True, style='-o', figsize=(10, 8), xlim=[10, 11000])
plot.set_xlabel('descending_array size')
plot.set_ylabel('time (sec)')
plt.savefig('/Users/home/PycharmProjects/Theory_of_computation/descending_array.png')

print("Success!")
