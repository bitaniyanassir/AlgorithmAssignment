import random
import time


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


list_lengths = [10, 100, 5000, 10000]  # List lengths to test

for length in list_lengths:
    # Generate a random list of the given length
    random_list = random.sample(range(1, length + 1), length)

    print(f"List Length: {length}")
    print("Random List:", random_list[:10])
    print("...")

    # Perform insertion sort on the random list and get the sorted list, comparison count, and elapsed time
    sorted_list, comparisons, elapsed_time = insertion_sort(random_list)

    print("Sorted List:", sorted_list[:10])
    print("...")
    print(f"Number of Comparisons: {comparisons}")
    print(f"Elapsed Time: {elapsed_time} seconds")
    print("---------------------")
