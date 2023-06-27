# Let's define an array of numbers to sort.
Arr = [10, 8, 25, 32, 42, 17, 31, 40]

# Now, we'll define a function called mergesort that will sort the array.
def mergesort(Arr):
  # First, we check if the length of the array is less than 2.
  # If it is, then it means the array is already sorted or empty,
  # so we can just return it as it is.
  if len(Arr) < 2:
    return Arr;

  # If the array has more than 1 element, we need to divide it into two halves.
  # We find the middle index of the array.
  mid = len(Arr) // 2

  # We create two new arrays by splitting the original array in half.
  left_Arr = Arr[:mid]
  right_Arr = Arr[mid:]

  # Now, we gotta do some fancy recursion stuff!
  # We call mergesort function again on the left and right halves
  # until we've got little tiny arrays that can't be divided anymore.
  mergesort(left_Arr)
  mergesort(right_Arr)

  # After sorting the left and right halves, we merge them back together into the original array.
  merge(left_Arr, right_Arr, Arr)

# The merge function takes in two sorted arrays (left and right) and merges them
# into a single sorted array (Arr).
def merge(left, right, Arr):
  i = 0  # index for the left array
  j = 0  # index for the right array
  k = 0  # index for the merged array

  # We compare the elements from both the left and right arrays and
  # put them in the merged array in the correct order.
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      Arr[k] = left[i]
      i += 1
    else:
      Arr[k] = right[j]
      j += 1
    k += 1

  # If there are any leftover elements in the left array, we copy them to the merged array.
  while i < len(left):
    Arr[k] = left[i]
    i += 1
    k += 1

  # If there are any leftover elements in the right array, we copy them to the merged array.
  while j < len(right):
    Arr[k] = right[j]
    k += 1
    j += 1

# Now, it's time to put the magic to work!
mergesort(Arr)

# Finally, we proudly present the sorted array.
print(Arr)
