import time
import matplotlib


def insertion_sort(arr):
    start_time = time.time()  # Start the timer
    comparisons = 0  # Counter for comparison operations

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1  # Increment the comparison counter

        arr[j + 1] = key

    end_time = time.time()  # Stop the timer

    return arr, comparisons, end_time - start_time


descending_list_lengths = [10, 100, 5000, 10000]  # List lengths to test

for length in descending_list_lengths:
    # Generate a list of the given length in descending order
    descending_list = list(range(length, 0, -1))

    # Print the descending list
    print(f"Descending List ({length} elements): ")
    print(descending_list[:10])
    print("...")

    # Perform insertion sort on the descending list and get the sorted list, comparison count, and elapsed time
    sorted_list, comparisons, elapsed_time = insertion_sort(descending_list)

    # Print the sorted list
    print(f"Sorted List ({length} elements): ")
    print(sorted_list[:10])
    print("...")

    print(f"Number of Comparisons: {comparisons}")
    print(f"Elapsed Time: {elapsed_time} seconds")
    print("---------------------")
