import sys
sys.setrecursionlimit(10001)

class Node:
    def __init__(self,key, data):
        self.data = data
        self.key =key
        self.left=None
        self.right=None
        self.p=None


class BST:
    def __init__(self,root=None):
        self.root=root

    def  insert(self,key,data):
        new_node=Node(key,data)

        y=None
        x=self.root
        while x!=None:
            y=x
            if new_node.key<x.key:
                x=x.left
            else :
                x=x.right

        new_node.p=y
        if y==None:
            self.root=new_node
        elif new_node.key<y.key:
            y.left=new_node
        else:
            y.right=new_node
    

    def transplant(self,u,v):
        if u.p ==None:
            self.root=v    # u become node
            
        elif u==u.p.left:  #if u is one the left
            u.p.left=v
        else:              #if u is on the right
            u.p.right=v

        if v!=None: # in case o not delete (v is a node)
            v.p=u.p
    


    def search(self,key):
        x=self.root
        while x!=None and key!=x.key:
            if key<x.key:
                x=x.left
            else :
                x=x.right
        return x
    

    def maximum(self,x):
        while x.right!=None:
            x=x.right
        return x
    

    def minimum(self,x):
        while x.left!=None:
            x=x.left
        return x

    def delete(self,delete):
        nodedelete=self.search(delete)   #if there is no left child, them repace it with right child
        if nodedelete.left==None:
            self.transplant(nodedelete,nodedelete.right)

        elif nodedelete.right==None:           # if there is no right childe, replace it with left child;
            self.transplant(nodedelete,nodedelete.left)

        else:
            y=self.minimum(nodedelete.right) 
            if y.p==nodedelete:
                self.transplant(nodedelete,y.right)     
                y.right=nodedelete.right
                y.right.p=y
            
            self.transplant(nodedelete,y)
            y.left=nodedelete.left
            y.left.p=y

    

    def predecessor(self,key):#the predecessor of a node is the node that comes immediately before the given node in an in-order traversal of the tree.
                            # eg 35 ma lr khin 24 lr tr lo myo
        nodeX=self.search(key)
        if nodeX.left==None:
            return None#no left child
        if nodeX.left!=None:
            return self.maximum(nodeX.left)
        
        y=nodeX.p
        while y != None and nodeX==y.left:
            nodeX=y
            y=y.p
        return y
    

    def successor(self,key):# opposite of predecessor
        nodeX=self.search(key)
        if nodeX.right==None:
            return
        if nodeX.right !=None:
            return self.minimum(nodeX.right)
        
        y=nodeX.p
        while y != None and nodeX==y.right:
            nodeX=y
            y=y.p
        return y


    def inorderwalk(self):
        result = []

        def inorder(node):
            if node is not None:
                inorder(node.left)
                result.append(node.key)
                inorder(node.right)

        inorder(self.root)
        return result
    
        
    def preorderwalk(self):
        result = []

        def preorder(node):
            if node is not None:
                result.append(node.key)
                preorder(node.left)
                preorder(node.right)

        preorder(self.root)
        return result

    def postorderwalk(self):
        result = []

        def postorder(node):
            if node is not None:
                postorder(node.left)
                postorder(node.right)
                result.append(node.key)

        postorder(self.root)
        return result

    def levelorderwalk(self):
        result = []

        if self.root is None:
            return result

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result


# Create an instance of the BST class
tree = BST()

# Insert keys into the binary search tree
keys_to_insert = [56, 70, 30, 60, 65, 22, 11, 16, 40, 95, 62,63, 3, 67]
for key in keys_to_insert:
    tree.insert(key, data=None)

# Print the inorder traversal of the tree
print("In-Order Traversal:", tree.inorderwalk())
# print("Pre-Order Traversal:", tree.preorderwalk())
# print("Post-Order Traversal:", tree.postorderwalk())
# print("Level-Order Traversal:", tree.levelorderwalk())



# ##key searching
# key_to_search = 2
# print("Search for key:", key_to_search)
# search_result = tree.search(key_to_search)
# if search_result:
#     print("Key found. Data:", search_result.data)
# else:
#     print("Key not found.")



# Test the delete operation
key_to_delete = 40
print("Deleting key:", key_to_delete)
tree.delete(key_to_delete)



# Print the inorder traversal after deletion
print("In-Order Traversal after deletion:", tree.inorderwalk())



# Test the maximum function
max_node = tree.maximum(tree.root)
print("Maximum node key:", max_node.key)

# Test the minimum function
min_node = tree.minimum(tree.root)
print("Minimum node key:", min_node.key)


#predecessor
predecessor_key = 63
predecessor = tree.predecessor(predecessor_key)
if predecessor:
    print("Predecessor of", predecessor_key, "is", predecessor.key)
else:
    print("No predecessor found for", predecessor_key)






def binary_tree():
    pass 
        
    # A binary tree is a fundamental data structure used in computer science to organize and store data in a hierarchical manner.
    #  It consists of nodes connected by edges, where each node contains a value and can have at most two children – a left child and a right child.
    #  The first node, typically called the "root," serves as the starting point for traversing the tree.
    # Binary trees offer a natural way to represent hierarchical relationships.
    #  They are used for a wide range of applications, including databases, file systems, and algorithms. 
    # The structure of a binary tree allows for efficient searching, insertion, and deletion operations when compared to linear data structures like arrays.
    # Binary trees come in various forms, such as binary search trees (BSTs), where nodes are arranged such that the left child of a node contains values less than the node's value, and the right child contains values greater than the node's value. 
    # This property enables fast retrieval and manipulation of data, making BSTs valuable for tasks like searching and sorting.
    # However, if the tree becomes unbalanced (one branch significantly longer than the other), performance may degrade. 
    # Techniques like balancing algorithms (e.g., AVL trees and Red-Black trees) address this issue.
    # In summary, binary trees provide a versatile foundation for structuring data, facilitating efficient operations, and enabling the development of advanced algorithms that underpin much of modern computing.
    #  Understanding binary trees is crucial for anyone working in computer science, as they serve as a building block for more complex data structures and algorithms.
def time_complexity():
    pass
    #The time complexity of operations on a binary tree can vary depending on the type of operation and the specific characteristics of the tree. Here, I'll provide an overview of the time complexities for some common binary tree operations:

    # 1. **Search Operation** (in a binary search tree):
    #    - Average Case: O(log n)
    #    - Worst Case (unbalanced tree): O(n)

    # 2. **Insertion Operation** (in a binary search tree):
    #    - Average Case: O(log n)
    #    - Worst Case (unbalanced tree): O(n)

    # 3. **Deletion Operation** (in a binary search tree):
    #    - Average Case: O(log n)
    #    - Worst Case (unbalanced tree): O(n)

    # 4. **Traversal Operations** (in-order, pre-order, post-order, level-order):
    #    - O(n), where n is the number of nodes in the tree. Each node is visited exactly once during traversal.

    # 5. **Finding Minimum/Maximum Element** (in a binary search tree):
    #    - Average Case: O(log n)
    #    - Worst Case (unbalanced tree): O(n)

    # 6. **Balancing Operations** (e.g., AVL tree, Red-Black tree):
    #    - Balancing operations have additional complexities associated with maintaining the balance of the tree after insertions and deletions. In AVL trees, for example, these operations have a time complexity of O(log n) due to the balancing rotations required.

    # 7. **Finding Predecessor/Successor** (in a binary search tree):
    #    - Average Case: O(log n)
    #    - Worst Case (unbalanced tree): O(n)

    # It's important to note that the time complexities mentioned above assume a balanced binary tree. In the worst case, where the tree is highly unbalanced (resembling a linked list), the time complexity can degrade to O(n) for search, insertion, deletion, and related operations. To mitigate this issue, self-balancing binary trees like AVL trees or Red-Black trees are used, which ensure that the tree remains balanced and maintains logarithmic time complexities for these operations.

    # In summary, the time complexity of binary tree operations depends on the specific operation being performed and the balance of the tree. Balancing techniques can help ensure that the worst-case time complexities are minimized, making binary trees efficient data structures for various applications.
def transplant():
    pass

    # Transplant is a fundamental operation used in binary search trees (BSTs) when removing a node while maintaining the binary search tree properties.
    #  It involves replacing one subtree with another subtree, effectively moving one subtree to another position within the tree.
    # The transplant operation is commonly used in the context of deleting a node from a binary search tree.
    #  When you want to delete a node, you need to replace it with another node from the tree while ensuring that the binary search tree properties are preserved.
    # Here's how the transplant operation works:\
    # Identify the parent of the node you want to replace (the "old node").
    # Determine whether the old node is a left child or a right child of its parent.
    # Set the appropriate child of the old node's parent to the new node that you want to replace the old node with.
    # If the new node is not None, update its parent pointer to point to the old node's parent.
    # The transplant operation effectively "cuts out" the old node from the tree and replaces it with the new node.
    # Transplanting nodes is crucial in maintaining the binary search tree structure after deletion.
    #  It ensures that the tree remains balanced and retains its ordering properties.
    #  Transplanting can be used in conjunction with other operations, such as finding the predecessor or successor of a node, to facilitate efficient deletion and manipulation of tree nodes.
    # In summary, the transplant operation is a key mechanism for maintaining the integrity of a binary search tree when nodes are deleted or moved, helping to keep the tree's structure and properties intact.
def deletion():
    pass
    # Deletion Operation in a Binary Search Tree (BST):
    # Deletion in a binary search tree involves removing a node while maintaining the binary search tree property
    #  – for each node, all nodes in its left subtree have values less than the node, and all nodes in its right subtree have values greater than the node.
    # The deletion process can be divided into three cases based on the number of children the node to be deleted has:
    # Node with No Children (Leaf Node):
    # In this case, you simply remove the node from the tree. If the node to be deleted is the root, set the root to None.
    # Node with One Child:
    # Replace the node to be deleted with its only child. If the node to be deleted is the root, replace it with its child. Update the parent reference of the child to point to the parent of the node being deleted.
    # Node with Two Children:
    # Find the in-order successor (or predecessor) of the node to be deleted. Copy the value of the successor (or predecessor) to the node to be deleted.
    #  Then, recursively delete the successor (or predecessor) node.
    # It's important to note that the choice between using the in-order successor or predecessor depends on the specific implementation and the requirements of the application.
    # Additionally, after deletion, if the tree becomes unbalanced, balancing techniques like notations (for example, in AVL trees) may be needed to maintain the desired height balance of the tree.
    # In summary, the deletion operation in a binary search tree involves carefully reorganizing the tree while ensuring that the binary search tree property is preserved. The specific steps and complexity can vary based on the type of deletion (node with no children, one child, or two children) and the balancing mechanisms employed in the tree.
def all_explained():
    pass
    # Insertion Function:
    # The insertion function adds a new node with a given key to the binary tree while preserving its hierarchical structure. 
    # Starting from the root, the function traverses the tree based on the key's value, moving left for smaller values and right for larger ones.
    #  It finds the appropriate spot for the new node and links it to its parent. Insertion in a balanced binary tree maintains efficient search and retrieval operations.

    # Deletion Function:
    # The deletion function removes a node with a specified key from the binary tree while maintaining its organization.
    #  Depending on the number of children, the function either directly removes a leaf node or restructures the tree while ensuring the binary search property is preserved.
    #  For nodes with two children, it identifies the in-order successor or predecessor to maintain ordering. Post-deletion, the tree may be rebalanced to avoid performance degradation in case of skewed trees.

    # Search Function:
    # The search function determines whether a node with a given key exists in the binary tree
    # Starting from the root, the function traverses the tree by comparing the key with node values. 
    # It moves left for smaller keys and right for larger ones. If the desired key is found, the function returns the corresponding node; otherwise, it returns a null value.
    #  Binary tree search leverages the tree's ordered structure, allowing for efficient retrieval of specific values.

    # In-Order Traversal:
    # In-order traversal visits nodes of the binary tree in a left-root-right sequence. 
    # Starting from the leftmost node, the traversal recursively explores left subtrees, then processes the current node, and finally traverses right subtrees. 
    # In-order traversal of a binary search tree yields elements in ascending order. 
    # This technique is commonly used to retrieve elements in sorted order, perform operations that require values to be processed in a specific order, or create a sorted representation of the tree.

    # Pre-Order Traversal:
    # Pre-order traversal explores nodes in a root-left-right order. 
    # Starting from the root, the traversal processes the current node, then moves to the left subtree, and finally traverses the right subtree. 
    # It's useful for creating a copy of the tree or evaluating expressions represented by expression trees.
    #  Additionally, pre-order traversal is employed in constructing prefix notation for arithmetic expressions.

    # Post-Order Traversal:
    # Post-order traversal visits nodes in a left-right-root order. S
    # tarting from the leftmost leaf, the traversal recursively explores left and right subtrees before processing the current node. 
    # This approach is useful for releasing resources associated with nodes in memory management or for evaluating expressions represented by expression trees. 
    # In binary search trees, post-order traversal can be used to delete nodes while maintaining the tree's structure.

    # Level-Order Traversal:
    # Level-order traversal explores nodes of the binary tree by level, from left to right. 
    # It starts at the root and processes nodes at each level before moving to the next level. 
    # This traversal is performed using a queue data structure to ensure that nodes at the same level are visited before moving deeper into the tree. 
    # Level-order traversal is essential for tasks like creating a breadth-first search or evaluating the width of the tree.

    # Successor Function:
    # The successor function determines the node with the smallest key greater than a given key in a binary search tree. 
    # Starting from the root, the function traverses the tree based on the key's value. If the key is found, it identifies the smallest key in the right subtree, if present. 
    # If not, it identifies the smallest ancestor with a larger key. 
    # Successor identification aids in finding the next value in ascending order and is used in various algorithms, including deleting nodes with two children.

    # Predecessor Function:
    # The predecessor function identifies the node with the largest key smaller than a given key in a binary search tree. 
    # Similar to the successor function, it traverses the tree based on the key's value. 
    # If the key is found, it locates the largest key in the left subtree, if present. 
    # If not, it identifies the largest ancestor with a smaller key. Predecessor determination is useful for retrieving the previous value in ascending order and is involved in tasks like finding the median.

    # These functions collectively form the core operations and traversal techniques that enable efficient organization, manipulation, and retrieval of data in binary trees.
def exanmple_adding():
    pass
    # Certainly, I can walk you through the step-by-step process of inserting each element from the list `A = [5, 6, 4, 7, 3, 8, 3, 9, 2, 0, 1]` into a binary search tree. Let's visualize the tree as we insert each element:

    # Initial Tree (Empty):
    # ```
    #     None
    # ```

    # Insert 5:
    # ```
    #      5
    #     / \
    # None   None
    # ```

    # Insert 6:
    # ```
    #      5
    #     / \
    # None    6
    #          \
    #          None
    # ```

    # Insert 4:
    # ```
    #      5
    #     / \
    #    4   6
    #   /     \
    # None     None
    # ```

    # Insert 7:
    # ```
    #      5
    #     / \
    #    4   6
    #         \
    #          7
    #           \
    #           None
    # ```

    # Insert 3:
    # ```
    #      5
    #     / \
    #    4   6
    #   /     \
    #  3       7
    #           \
    #            None
    # ```

    # Insert 8:
    # ```
    #      5
    #     / \
    #    4   6
    #   /     \
    #  3       7
    #           \
    #            8
    #             \
    #             None
    # ```

    # Insert 3 (Duplicate, inserted on the left):
    # ```
    #      5
    #     / \
    #    4   6
    #   /     \
    #  3       7
    # /         \
    # 3          8
    #             \
    #             None
    # ```

    # Insert 9:
    # ```
    #      5
    #     / \
    #    4   6
    #   /     \
    #  3       7
    # /         \
    # 3          8
    #             \
    #              9
    #               \
    #               None
    # ```

    # Insert 2:
    # ```
    #      5
    #     / \
    #    4   6
    #   /     \
    #  3       7
    # /         \
    # 3          8
    # /          \
    # 2           9
    #             /
    #           None
    # ```

    # Insert 0:
    # ```
    #      5
    #     / \
    #    4   6
    #   /     \
    #  3       7
    # /         \
    # 3          8
    # /          \
    # 2           9
    # /             \
    # 0             None
    # ```

    # Insert 1:
    # ```
    #      5
    #     / \
    #    4   6
    #   /     \
    #  3       7
    # /         \
    # 3          8
    # /          \
    # 2           9
    # /             \
    # 0             None
    #  \
    #   1
    # ```

    # This sequence of insertions results in the creation of a binary search tree with the given elements. Keep in mind that the final structure of the tree can vary depending on the order of insertions and the specific balancing mechanisms used. In this case, the tree may not be perfectly balanced due to the order of insertions.