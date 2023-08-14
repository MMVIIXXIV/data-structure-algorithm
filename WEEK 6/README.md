
# Binary Search Tree (BST) README

A Binary Search Tree (BST) is a fundamental data structure used in computer science for efficient storage and retrieval of data. It is a type of binary tree where each node has at most two children, commonly referred to as the left child and the right child. The property that makes a BST special is that for each node:

- All nodes in the left subtree have values less than the node's value.
- All nodes in the right subtree have values greater than the node's value.

This property ensures that data in a BST is organized in a way that allows for efficient search, insertion, and deletion operations.

## Operations

1. **Insertion**: To insert a new element into the BST, we compare the value of the new element with the current node and decide whether to move left or right. We repeat this process until we find an empty spot to insert the new element.

2. **Search**: Searching in a BST involves comparing the target value with the value of the current node. If the values match, the search is successful. Otherwise, we move left or right based on the comparison and repeat the process in the appropriate subtree.

3. **Deletion**: Deleting a node from a BST involves three cases:
   - Node has no children: Simply remove the node.
   - Node has one child: Remove the node and replace it with its child.
   - Node has two children: Find the inorder successor (the smallest node in the right subtree), replace the node's value with the inorder successor's value, and then delete the inorder successor.

## Time Complexity

The time complexity of basic operations in a Binary Search Tree depends on the height of the tree. In a well-balanced BST, the height is logarithmic in the number of nodes (logarithmic base 2).

- **Insertion**: O(log n) - On average, inserting an element takes O(log n) time in a balanced BST.
- **Search**: O(log n) - Similarly, searching for an element takes O(log n) time on average in a balanced BST.
- **Deletion**: O(log n) - Deletion also takes O(log n) time on average in a balanced BST.

However, if the BST is not balanced and becomes skewed (essentially forming a linked list), the time complexity of these operations can degrade to O(n), where n is the number of nodes.

## Conclusion

Binary Search Trees are versatile data structures that offer efficient storage and retrieval of data when balanced properly. It is important to maintain the balance of a BST to ensure optimal time complexity for its operations. Understanding the properties and operations of BSTs is crucial for building more complex data structures and algorithms.

For implementation examples and practical usage of Binary Search Trees, check out the provided code samples and explore the algorithms further.

--- 
 
