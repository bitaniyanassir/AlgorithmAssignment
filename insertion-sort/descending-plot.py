import random
import time
import matplotlib.pyplot as plt


def insertion_sort_comparison_count(arr):
    comparisons = 0  # Counter for comparison operations

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1  # Increment the comparison counter

        arr[j + 1] = key

    return comparisons


list_lengths = [10, 100, 500, 1000, 5000]  # List lengths to test
comparison_counts_asc = []
# List to store the number of comparisons for descending lists
comparison_counts_desc = []

for length in list_lengths:

    # Generate descending list
    descending_list = list(range(length, 0, -1))

    # Perform insertion sort on descending list and get the comparison count
    comparison_count_desc = insertion_sort_comparison_count(descending_list)
    comparison_counts_desc.append(comparison_count_desc)

# Plotting the number of comparisons against the length of the lists
plt.plot(list_lengths, comparison_counts_desc, marker='o', label='Descending')
plt.xlabel('List Length')
plt.ylabel('Number of Comparisons')
plt.title('Number of Comparisons vs List Length')
plt.legend()
plt.show()
