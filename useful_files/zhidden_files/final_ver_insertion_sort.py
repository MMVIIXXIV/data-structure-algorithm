# Function to perform insertion sort on an array 'arr'
def insort(arr):
    for i in range(len(arr)):
        key = arr[i]  # Current element to be inserted at the right position
        j = i - 1  # Index of the previous element

        # Move elements of 'arr[0...i-1]' that are greater than 'key' to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1

        arr[j + 1] = key  # Insert the 'key' at its correct position in the sorted subarray


import time

# Input: Take a list of integers from the user and store it in 'arr'
arr = list(map(int, input().split()))

n = len(arr)

# Record the start time
start_time = time.time()

# Call the insort function to sort the 'arr' using insertion sort
insort(arr)

# Record the end time
end_time = time.time()

# Print the sorted list 'arr'
print(arr)

# Calculate and print the time taken for sorting
print("Time taken:", end_time - start_time, "seconds")


# The insort function implements the insertion sort algorithm, which sorts an array by inserting each element into its correct position within the already sorted subarray to its left.

# The outer loop iterates through the array arr, and for each element, the inner loop iterates through the already sorted subarray to find the correct position for insertion.

# Inside the inner loop, elements that are greater than the current key are shifted one position to the right to make space for the insertion of the key.

# The key is then inserted at its correct position in the sorted subarray.

# The input list of integers is taken from the user and stored in the array arr.

# The insort function is called to sort the array arr using the insertion sort algorithm.

# The sorted array arr is printed to the console.

# The time taken for sorting is measured using the time module and printed.

# Time Complexity:

# Best Case: O(n) - If the input array is already sorted, each element is compared to only one previous element before being placed in its correct position.
# Worst Case: O(n^2) - If the input array is sorted in reverse order, each element may need to be compared with and shifted by every previous element.
# Insertion sort is efficient for small datasets and can perform well when the input array is nearly sorted. However, for larger datasets, algorithms like merge sort or quicksort are generally more efficient due to their better average-case time complexity.
