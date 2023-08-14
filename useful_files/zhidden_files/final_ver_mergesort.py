# Function to merge two sorted arrays 'left' and 'right' into 'arr'
def merge(left, right, arr):
    nl = len(left)  # Calculate the length of the 'left' array
    nr = len(right)  # Calculate the length of the 'right' array
    i, j, k = 0, 0, 0  # Initialize pointers for 'left', 'right', and 'arr'

    # Compare elements from 'left' and 'right' and merge them into 'arr'
    while i < nl and j < nr:
        if left[i] < right[j]:  # Compare elements from 'left' and 'right'
            arr[k] = left[i]    # Place the smaller element into 'arr'
            i += 1              # Move the pointer in 'left'
        else:
            arr[k] = right[j]   # Place the smaller element into 'arr'
            j += 1              # Move the pointer in 'right'
        k += 1                  # Move the pointer in 'arr'

    # Handle remaining elements in 'left' and 'right'
    while i < nl:
        arr[k] = left[i]        # Place remaining elements from 'left' into 'arr'
        i += 1
        k += 1
    while j < nr:
        arr[k] = right[j]       # Place remaining elements from 'right' into 'arr'
        j += 1
        k += 1


# Function to perform merge sort on an array 'arr'
def mergesort(arr):
    if len(arr) <= 1:           # Base case: If array has 1 or 0 elements, it's already sorted
        return arr
    mid = len(arr) // 2         # Calculate the middle index of the array
    left = arr[:mid]            # Divide the array into two halves: 'left' and 'right'
    right = arr[mid:]
    mergesort(left)            # Recursively sort the 'left' half
    mergesort(right)           # Recursively sort the 'right' half
    merge(left, right, arr)    # Merge the sorted 'left' and 'right' halves into 'arr'


# Input: Take a list of integers from the user and store it in 'testcase'
testcase = list(map(int, input().split(",")))

# Perform merge sort on 'testcase' list
mergesort(testcase)

# Print the sorted list 'testcase'
print(testcase)


# The merge function takes two sorted arrays (left and right) and merges them into a single sorted array (arr).

# It uses three pointers i, j, and k to iterate through left, right, and arr respectively. It compares elements from left and right, placing the smaller element into arr at index k. The pointers i, j, and k are incremented accordingly.

# After merging, any remaining elements in left and right are added to the end of arr.

# The mergesort function recursively divides the input array into two halves (left and right) until the base case is reached (array has 1 or 0 elements).

# It then sorts the two halves separately using recursive calls to mergesort and finally merges them back together using the merge function.

# The input list of integers is taken from the user, and then the mergesort function is called to sort the list.

# The sorted list is printed to the console.


# Dividing the array into two halves (left and right) in the mergesort function takes constant time, O(1).


# The recursive calls to mergesort on the two halves result in the array being divided into smaller and smaller halves until it reaches the base case of having 1 or 0 elements.
#  This process continues until each element is in its own separate array. The number of recursive calls is proportional to the number of elements in the input array, which is O(n), where n is the number of elements.
# The merge function iterates through both the left and right arrays exactly once, comparing and merging elements.
#  In the worst case, it performs n comparisons and n assignments, where n is the total number of elements in the input array.
# Combining these factors, the overall time complexity of the merge sort algorithm is O(n log n), where n is the number of elements in the input array.
#  This is because the array is repeatedly divided in half during the recursion, and at each level of recursion, a linear amount of work (O(n)) is done during the merging phase.