import time
import random
import matplotlib.pyplot as plt


def merge_sort(arr):
    operations = 0

    if len(arr) <= 1:
        return arr, operations

    mid = len(arr) // 2
    left_half, left_ops = merge_sort(arr[:mid])
    right_half, right_ops = merge_sort(arr[mid:])
    operations += left_ops + right_ops

    sorted_list, merge_ops = merge(left_half, right_half)
    operations += merge_ops

    return sorted_list, operations


def merge(left, right):
    merged = []
    operations = 0
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
        operations += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
        operations += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
        operations += 1

    return merged, operations


list_lengths = [10, 100, 500, 1000, 5000]
descending_ops = []

for length in list_lengths:
    descending_list = list(range(length, 0, -1))
    start_time = time.time()
    _, descending_op = merge_sort(descending_list)
    descending_ops.append(descending_op)
    end_time = time.time()

plt.plot(list_lengths, descending_ops, label='Descending List')
plt.xlabel('List Length')
plt.ylabel('Number of Operations')
plt.title('Merge Sort: Number of Operations vs List Length')
plt.legend()
plt.show()
