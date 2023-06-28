# This code uses the QuickSort algorithm to sort a list of numbers.

# Function to partition the list and find the pivot index
def partition(arr, start, end):
  pivot = arr[end]  # Choose the last element of the list as the pivot
  pIndex = start  # Initialize the partition index to the start of the list

  # Iterate over the elements in the range from start to end - 1
  for i in range(start, end):
    if arr[i] <= pivot:  # If the current element is less than or equal to the pivot
      # Swap the current element with the element at the partition index
      arr[i], arr[pIndex] = arr[pIndex], arr[i]
      pIndex += 1  # Increment the partition index

  # Swap the pivot with the element at the partition index
  arr[pIndex], arr[end] = arr[end], arr[pIndex]
  return pIndex  # Return the partition index

# Function to perform QuickSort recursively
def QuickSort(arr, start, end):
  if start < end:  # If there is more than one element in the list
    # Find the partition index
    pIndex = partition(arr, start, end)
    # Recursively sort the elements before the partition index
    QuickSort(arr, start, pIndex - 1)
    # Recursively sort the elements after the partition index
    QuickSort(arr, pIndex + 1, end)

arr = [7, 2, 1, 6, 8, 5, 3, 4]  # The list of numbers to be sorted
QuickSort(arr, 0, len(arr) - 1)  # Call the QuickSort function to sort the list
print(arr)  # Print the sorted list
