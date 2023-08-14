'''
+----------------+------------------------------------------+
| Function       | Job                                      |
+----------------+------------------------------------------+
| buildHeap(arr) | - Converts the input array into a valid  |
|                |   binary max heap by calling heapify on  |
|                |   non-leaf nodes in reverse order.       |
|                |                                          |
|                | - It ensures the largest element (root)  |
|                |   is at the top of the heap.             |
+----------------+------------------------------------------+
| heapify(arr, i)| - Restores the heap property for the     |
|                |   subtree rooted at index i.             |
|                |                                          |
|                | - Compares the value at index i with its |
|                |   left and right children (if any).      |
|                |                                          |
|                | - Swaps elements to move the largest     |
|                |   value to the root of the subtree.      |
|                |                                          |
|                | - Recursively calls heapify on the       |
|                |   affected sub-tree to maintain the heap |
|                |   property down the sub-tree.            |
+----------------+------------------------------------------+
| heap_sort(arr) | - Creates a max heap from the input      |
|                |   array using buildHeap function.        |
|                |                                          |
|                | - Extracts the maximum element (root)    |
|                |   from the max heap and appends it to    |
|                |   the sorted array.                      |
|                |                                          |
|                | - Repeats the extraction process until   |
|                |   the heap becomes empty.                |
|                |                                          |
|                | - Returns the sorted array with elements |
|                |   arranged in ascending order.           |
+----------------+------------------------------------------+
| extractMax(arr)  | - Extracts the maximum element (root)  |
|                  |   from the max heap.                   |
|                  |                                        |
|                  | - Replaces the root with the last      |
|                  |   element of the heap.                 |
|                  |                                        |
|                  | - Reduces the size of the heap.        |
|                  |                                        |
|                  | - Calls heapify on the root element to |
|                  |   restore the heap property.           |
|                  |                                        |
|                  | - Returns the extracted maximum element|
+------------------+----------------------------------------+
'''


class Heap:
    def __init__(self,items):
        self.a=items
        self.heapsize=len(self.a)
        if len(self.a)>=1:
            self.buildHeap()

    def buildHeap(self):
        for i in range((self.heapsize - 1) // 2, -1, -1):
            self.heapify(i)
    def empty(self):
        if self.heapsize==0:
            return True
        return False

    def heapify(self,i):
        largest=i
        left=(i*2)+1
        right=(i+1)*2
        if left<self.heapsize and self.a[left]       >    self.a[largest]:
            largest=left
        if right<self.heapsize and self. a[right]     >     self.a[largest]:
            largest=right
        if largest!=i:
            self.a[largest],self.a[i] =self.a[i],self.a[largest]
    
    def extract(self):

        maximum=self.a[0]
        last_element=self.heapsize-1
        self.a[0],self.a[last_element]=self.a[last_element],self.a[0]
        self.heapsize-=1
        self.heapify(0)
        return maximum
    
    def insert(self,x):
        self.heapsize+=1
        if len(self.a)<self.heapsize :
            self.a.append(x)
        else :
            self.a[self.heapsize-1]=x
        j=self.heapsize-1# heap
        k=(j-1)//2       #parent
        while j>0 and  self.a[j]      >        self.a[k]:
            self.a[j],self.a[k]=self.a[k],self.a[j]
            j=k
            k=(j-1)//2

def heap_sort(arr):
    h = Heap(arr)
    sorted_arr = []
    while not h.empty():
        sorted_arr.append(h.extract())
    return sorted_arr

h = Heap([1,2,3,4,5,6,7,8,9,10])
h.insert(0)
h.insert(199)
h.insert(34)
h.insert(2)
h.insert(1)
h.insert(9)
h.insert(8)

# Now, you can use the heap_sort function to sort the elements already inserted into the heap.
sorted_arr = heap_sort(h.a)
print(sorted_arr)
 


# #Heap:
# A heap is a specialized tree-based data structure that satisfies the heap property.
#  The heap property states that for a min-heap, every parent node has a value less than or equal to the values of its children, and for a max-heap, every parent node has a value greater than or equal to the values of its children.
#  Heaps are commonly used to implement priority queues and for efficient sorting algorithms like heapsort.

# A binary heap is a common type of heap that is structured as a binary tree. Binary heaps can be efficiently stored in arrays,
#  where the children of an element at index i are located at indices 2i + 1 (left child) and 2i + 2 (right child), and the parent of an element at index i is located at index (i - 1) / 2.

# Heapify:
# Heapify is an operation that ensures that the heap property is maintained in a binary heap.
#  It takes an array (which may not satisfy the heap property) and rearranges its elements to satisfy the heap property. There are two main steps in heapify:

# Heapify Down (also known as "Sink"): Starting from a given node, you compare its value with the values of its children. If it violates the heap property, 
# you swap it with the smaller (in a min-heap) or larger (in a max-heap) child, and then continue the process recursively down the tree until the heap property is satisfied.


# Heapify Up (also known as "Swim"): This operation is used when you insert an element into the heap.
#  You compare the element with its parent, and if it violates the heap property, you swap it with its parent and repeat the process until the heap property is satisfied.

# Heapify is crucial for various heap-related operations to maintain the efficient structure and properties of the heap.





# def heap_sort(arr):
#     h = Heap(arr)
#     sorted_arr = []
#     while not h.empty():
#         sorted_arr.append(h.extract())
#     return sorted_arr

# arr=[0,1,9,2,8,3,8,4,5,7,6,0]

# soted_arr=heap_sort(arr)
# print(soted_arr)


def breakdown():
    pass
    # heap class:

    # The heap class is used to create and manage a max-heap.
    # The __init__ method initializes the heap with an optional list of items, which represent the initial elements of the heap.
    # The buildHeap method is responsible for building the max-heap from the given list of items.
    # The heapify method is used to restore the max-heap property for a node at a given index.
    # The extract method removes and returns the maximum element (root) from the heap, restoring the heap property afterward.
    # heap_sort function:

    # The heap_sort function takes an input array, constructs a max-heap using the heap class, and then repeatedly extracts the maximum element from the heap to sort the input array.
def insert():
    pass
    # The insert method is used to add an element to the heap while maintaining the heap property, 
    # which ensures that the parent nodes are smaller (in a min-heap) or greater (in a max-heap) than their child nodes.
    # Increase heapsize by 1 to reflect the new size of the heap after insertion.

    # Check if the current list size is less than the updated heapsize. If it is, append the new element x to the list. Otherwise, overwrite the value at the last position with x.

    # Initialize j with the index of the newly inserted element. Initialize k as the index of its parent.

    # Enter a loop that continues as long as j is greater than 0 (i.e., we haven't reached the root of the heap) and the value of the element at index j is smaller than the value of the parent at index k.

    # Swap the element at index j with its parent at index k.

    # Update j to the parent index k and calculate the new parent index k for the next iteration.

    # This loop essentially "bubbles up" the newly inserted element by swapping it with its parent as long as the heap property is violated. This ensures that the heap property is restored after inserting the new element.
def heap():
    #     The time complexity of common heap operations depends on the specific operation and the type of heap being used (min-heap or max-heap). 
    # Here are the time complexities for various heap operations using a binary heap (a common type of heap):

    # Insertion (Heapify Up):

    # Time Complexity: O(log n)
    # Explanation: When you insert an element into a binary heap, you need to perform the "heapify up" operation. 
    # This involves comparing the inserted element with its parent and swapping if necessary.
    #  This operation ensures that the heap property is maintained, and the height of the binary heap is log(n), where n is the number of elements in the heap. 
    # Therefore, the time complexity for insertion is O(log n).



    # Deletion (Heapify Down):
    # Time Complexity: O(log n)
    # Explanation: When you remove the root element (min or max) from a binary heap, you need to perform the "heapify down" operation.
    #  This involves swapping the root with the last leaf node and then comparing it with its children and swapping as needed to maintain the heap property. 
    # Like insertion, heapify down also takes O(log n) time since it ensures that the heap property is maintained and the height of the binary heap is log(n).
    
    
    
    # Peek (Accessing Root Element):
    # Time Complexity: O(1)
    # Explanation: Accessing the root element of a binary heap (peeking) is a constant-time operation, as the root is always at the top of the heap.




    # Building a Heap (Heapify All):

    # Time Complexity: O(n)
    # Explanation: Given an array of elements, you can build a heap by performing the heapify down operation on each non-leaf node. Since about half of the nodes in a binary heap are leaf nodes, the number of non-leaf nodes is roughly n/2. Therefore, the total time complexity to build a heap is O(n).
    # Heap Sort:

    # Time Complexity: O(n log n)
    # Explanation: Heap sort involves building a max-heap from the input array and repeatedly extracting the maximum element from the heap and restoring the heap property. The time complexity of heap sort is dominated by the building of the heap, which takes O(n), and the extraction of elements, which takes O(log n) per element extracted. Therefore, the overall time complexity of heap sort is O(n log n).
    pass