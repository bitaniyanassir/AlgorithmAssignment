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
random_ops = []

for length in list_lengths:
    random_list = random.sample(range(length), length)

    start_time = time.time()
    _, random_op = quick_sort(random_list)
    random_ops.append(random_op)
    end_time = time.time()

plt.plot(list_lengths, random_ops, label='Random List')
plt.xlabel('List Length')
plt.ylabel('Number of Operations')
plt.title('Quick Sort: Number of Operations vs List Length')
plt.legend()
plt.show()
