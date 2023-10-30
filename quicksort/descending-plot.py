
import time
import random
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10**6)  # Set a higher recursion limit


def quick_sort(arr):
    operations = 0

    if len(arr) <= 1:
        return arr, operations

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    less = []
    equal = []
    greater = []

    for element in arr:
        if element < pivot:
            less.append(element)
            operations += 1
        elif element == pivot:
            equal.append(element)
            operations += 1
        else:
            greater.append(element)
            operations += 1

    sorted_list, less_ops = quick_sort(less)
    sorted_list += equal
    sorted_list += quick_sort(greater)[0]
    operations += less_ops

    return sorted_list, operations


list_lengths = [10, 100, 500, 1000, 5000]
descending_ops = []

for length in list_lengths:
    descending_list = list(range(length, 0, -1))

    start_time = time.time()
    _, descending_op = quick_sort(descending_list)
    descending_ops.append(descending_op)
    end_time = time.time()

plt.plot(list_lengths, descending_ops, label='Descending List')
plt.xlabel('List Length')
plt.ylabel('Number of Operations')
plt.title('Quick Sort: Number of Operations vs List Length')
plt.legend()
plt.show()
