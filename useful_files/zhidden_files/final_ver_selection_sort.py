#choose either min/max of an array
#swap the position with current value (of the loop , in this case [index i] )
#repeat

# Function to perform selection sort on an array 'arr'
def selection_sort(arr):
    n = len(arr)  # Calculate the length of the array 'arr'

    # Iterate through the array up to the second-to-last element
    for i in range(len(arr) - 1):
        min_index = i  # Assume the current element is the minimum

        # Iterate through the unsorted part of the array to find the minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # Compare the current element with the assumed minimum
                min_index = j  # Update the index of the minimum element

        # Swap the current element with the minimum element found
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Input: Take a list of integers from the user and store it in 'arr'
arr = list(map(int, input().split()))

# Call the selection_sort function to sort the 'arr' using selection sort
selection_sort(arr)

# Print the sorted list 'arr'


# The selection_sort function implements the selection sort algorithm,
#  which sorts an array by repeatedly selecting the minimum element from the unsorted part of the array and swapping it with the first element of the unsorted part.

# The outer loop iterates through the array up to the second-to-last element (len(arr) - 1), as the last element will be automatically in the correct position after all the swaps.

# Inside the outer loop, the min_index variable is initialized to the current index i, assuming that the current element is the minimum.

# The inner loop (for j in range(i + 1, n)) iterates through the unsorted part of the array to find the index of the minimum element.
#  If an element smaller than the current assumed minimum is found, the min_index is updated to the index of that smaller element.

# After finding the minimum element in the unsorted part, a swap is performed between the current element at index i and the minimum element at index min_index. 
# This places the minimum element in its correct position in the sorted part of the array.

# The input list of integers is taken from the user and stored in the array arr.

# The selection_sort function is called to sort the array arr using the selection sort algorithm.

# The sorted array arr is printed to the console.







# The time complexity of the provided selection sort algorithm is O(n^2), where n is the number of elements in the input array. Here's how this time complexity is derived:

# 1. **Outer Loop:** The outer loop iterates through the array from the first element to the second-to-last element (i.e., `n - 1` iterations). This part contributes O(n) time complexity.

# 2. **Inner Loop:** Inside the outer loop, the inner loop iterates through the unsorted part of the array to find the minimum element. In the worst case, this inner loop also iterates through a significant portion of the array, specifically from the `(i + 1)`-th element to the last element (i.e., `(n - i - 1)` iterations). Since the outer loop runs for `n - 1` iterations and the inner loop iterations decrease with each iteration of the outer loop, the total number of iterations in the worst case is:

#    `(n - 1) + (n - 2) + (n - 3) + ... + 1 = (n - 1) * n / 2 = O(n^2)`

#    This is because the sum of the first `n - 1` natural numbers is given by `(n - 1) * n / 2`.

# 3. **Swaps:** Within each iteration of the inner loop, a swap operation is performed to place the minimum element in the correct position. The number of swaps is proportional to the number of inner loop iterations, which is O(n^2) in the worst case.

# Combining these factors, the overall time complexity of the selection sort algorithm is O(n^2). This quadratic time complexity makes selection sort inefficient for larger datasets, especially when compared to more advanced sorting algorithms like merge sort or quicksort, which have better average and worst-case time complexities.