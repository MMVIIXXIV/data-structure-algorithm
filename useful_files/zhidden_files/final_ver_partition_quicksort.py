import sys
import time


# Function to partition the array based on the pivot
def partition(arr, left, right):
    global COUNTER
    pivot = arr[right]  # Choose the rightmost element as the pivot
    index = left - 1  # Initialize the index of the smaller element

    # Iterate through the subarray from 'left' to 'right - 1'
    for j in range(left, right):
        COUNTER += 1  # Increment the counter for each loop iteration
        if arr[j] < pivot:
            index += 1
            # Swap the elements at 'index' and 'j' to move smaller elements to the left
            arr[index], arr[j] = arr[j], arr[index]

    # Place the pivot element in its correct position
    arr[right], arr[index + 1] = arr[index + 1], arr[right]
    return index + 1

# Recursive function to perform quicksort
def quicksort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)  # Find the partition index

        # Recursively sort the subarray before and after the partition
        quicksort(arr, left, p - 1)
        quicksort(arr, p + 1, right)



COUNTER=0
sys.setrecursionlimit(1000000)



#wrost case
st = time.process_time()
# A= list(map(int, input().split(" ")))
A=[8,4,3,1,6,7,11,9,2,10,5]
print(A)
quicksort(A,0,len(A)-1)
print(A)
et = time.process_time()
print(et-st)
print(COUNTER)




# #best case
# COUNTER=0
# st = time.process_time()
# A= list(map(int, input().split(" ")))
 
# print(A)
# quicksort(A,0,len(A)-1)
# print(A)
# et = time.process_time()
# print(et-st)
# print(COUNTER)


# The partition function takes an array arr, a left index left, and a right index right.
#  It selects the rightmost element as the pivot and rearranges the elements such that elements smaller than the pivot are on the left and elements greater than or equal to the pivot are on the right. 
# The function returns the index of the pivot element after partitioning.

# The quicksort function is a recursive function that sorts an array using the quicksort algorithm. 
# It takes the same parameters as the partition function: the array arr, a left index left, and a right index right.

# The quicksort algorithm selects a pivot element, partitions the array around the pivot, and then recursively sorts the subarrays before and after the pivot. 
# This process is repeated until the subarrays become single-element or empty arrays, at which point the sorting is complete.



# Time Complexity:


# In the worst case,The worst-case scenario for the quicksort algorithm occurs when the input array is already sorted (either in ascending or descending order).
#  when the pivot selection consistently results in an unbalanced partition (for example, selecting the smallest or largest element as the pivot), the quicksort algorithm can degrade to O(n^2) time complexity.

# However, on average and best-case scenarios, the time complexity of quicksort is O(n log n).
# The partitioning step takes O(n) time, and in each recursive call, the array is divided into roughly two halves. This results in the average and best-case time complexity of O(n log n) since the partitioning is performed at most log n times.