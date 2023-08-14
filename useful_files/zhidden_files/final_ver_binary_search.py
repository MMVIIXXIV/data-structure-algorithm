# Read input value K
K = int(input())

# Read and split the input numbers to create the list
lst = [int(i) for i in input().split(" ")]

# Function to perform binary search on a sorted list
def binarySearch(left, key, right):
    while left <= right:
        mid = (left + right) // 2
        if key == lst[mid]:
            return True
        elif key < lst[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False

# Sort the list in ascending order
lst.sort()

# Initialize a variable to track if a pair is found
found = False

# Iterate through the sorted list
for i in lst:
    y = K / i  # Calculate the other value for the pair
    found = binarySearch(0, y, len(lst) - 1)  # Search for the value 'y' in the list
    if found:
        break  # If pair is found, break the loop

# Check if a pair was found
if not found:
    print("No pair multiplies to K")
else:
    print(i, int(y))  # Print the pair that multiplies to K


# The code reads an integer K and a list of integers lst from the user.

# The binarySearch function performs binary search on a sorted list. 
# It searches for a given key in the range between indices left and right, updating the search range based on the comparison results. 
# It returns True if the key is found, and False otherwise.

# The input list lst is sorted in ascending order using the sort() method.

# The code iterates through the sorted list and calculates the value y = K / i, where i is the current element of the list. 
# It then searches for the value y in the list using the binarySearch function.

# If a pair of numbers that multiply to K is found (found becomes True), the loop breaks and the pair is printed.

# If no pair is found, the code prints "No pair multiplies to K."

# Best and Worst-Case Time Complexity:

# Best Case: If the first pair of numbers considered multiplies to K, the time complexity will be approximately O(log n) for the binary search step, where n is the number of elements in the list.
#  This is because the binary search can find the pair quickly without going through the entire list.

# Worst Case: If no pair is found until the end of the list, the binary search will be performed n times, 
# resulting in a worst-case time complexity of O(n * log n) due to the iteration through the list and the binary search for each element.

# Note: While the worst-case time complexity is O(n * log n) in this approach, 
# it's important to consider that it may not be the most optimal solution for finding a pair that multiplies to K, especially if the input list is large. Other algorithms, like using a hash set or sorting with two pointers, can achieve a linear time complexity of O(n) in the best and worst cases.