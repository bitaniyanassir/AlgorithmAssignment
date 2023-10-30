import time
import sys
sys.setrecursionlimit(10**6)


def quick_sort(arr):
    operations = 0

    if len(arr) <= 1:
        return arr, operations

    pivot = arr[0]
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


list_lengths = [10, 100, 5000, 10000]

for length in list_lengths:
    descending_list = list(range(length, 0, -1))  # Generate descending list

    start_time = time.time()
    sorted_list, descending_op = quick_sort(descending_list)
    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f"List Length: {length}")
    # Print the first ten numbers only
    print(f"Sample Input: {descending_list[:10]}")
    # Print the first ten numbers only
    print(f"Sample Sorted: {sorted_list[:10]}")
    print(f"Number of Operations: {descending_op}")
    print(f"Elapsed Time: {elapsed_time} seconds")
    print("=" * 50)
