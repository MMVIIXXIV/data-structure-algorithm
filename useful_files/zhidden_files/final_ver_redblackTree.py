
# Define Node
class RB_Node():
    def __init__(self,key, data=None):
        self.data = data
        self.key = key                                   # Key of Node
        self.p = None                                    # Parent of Node
        self.left = None                                 # Left Child of Node
        self.right = None                                # Right Child of Node
        self.color = 1                                   # Red Node as new node is always inserted as Red Node

# Define R-B Tree
class RBTree():
    def __init__(self):
        self.NULL = RB_Node ( 0 )
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL


    # Insert New Key
    def insert(self, key):
        node = RB_Node(key)
        node.p = None
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   # Set root colour as Red
        self.RB_Insert(node)

    # Insert New Node
    def RB_Insert(self, node):
        node.p = None
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   # Set root colour as Red
        
        y = None
        x = self.root

        while x != self.NULL :                           # Find position for new node
            y = x
            if node.key < x.key :
                x = x.left
            else :
                x = x.right

        node.p = y                                       # Set p of Node as y
        if y == None :                                   # If parent i.e, is none then it is root node
            self.root = node
        elif node.key < y.key :                          # Check if it is right Node or Left Node by checking the value
            y.left = node
        else :
            y.right = node

        if node.p == None :                              # Root node is always Black
            node.color = 0
            return

        if node.p.p == None :                            # If parent of node is Root Node
            return

        self.fixInsert ( node )                          # Else call for Fix Upj


    def Tree_Minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def Tree_Maximum(self, node):
        while node.right != self.NULL:
            node = node.right
        return node

    # Code for left rotate
    def LR ( self , x ) :
        y = x.right                                      # Y = Right child of x
        x.right = y.left                                 # Change right child of x to left child of y
        if y.left != self.NULL :
            y.left.p = x

        y.p = x.p                                        # Change parent of y as parent of x
        if x.p == None :                                 # If parent of x == None ie. root node
            self.root = y                                # Set y as root
        elif x == x.p.left :
            x.p.left = y
        else :
            x.p.right = y
        y.left = x
        x.p = y


    # Code for right rotate
    def RR ( self , x ) :
        y = x.left                                       # Y = Left child of x
        x.left = y.right                                 # Change left child of x to right child of y
        if y.right != self.NULL :
            y.right.p = x

        y.p = x.p                                        # Change parent of y as parent of x
        if x.p == None :                                 # If x is root node
            self.root = y                                # Set y as root
        elif x == x.p.right :
            x.p.right = y
        else :
            x.p.left = y
        y.right = x
        x.p = y


    # Fix Up Insertion
    def fixInsert(self, k):
        while k.p.color == 1:                            # While parent is red
            if k.p == k.p.p.right:                       # if parent is right child of its parent
                u = k.p.p.left                           # Left child of grandparent
                if u.color == 1:                         # if color of left child of grandparent i.e, uncle node is red
                    u.color = 0                          # Set both children of grandparent node as black
                    k.p.color = 0
                    k.p.p.color = 1                      # Set grandparent node as Red
                    k = k.p.p                            # Repeat the algo with Parent node to check conflicts
                else:
                    if k == k.p.left:                    # If k is left child of it's parent
                        k = k.p
                        self.RR(k)                       # Call for right rotation
                    k.p.color = 0
                    k.p.p.color = 1
                    self.LR(k.p.p)
            else:                                         # if parent is left child of its parent
                u = k.p.p.right                           # Right child of grandparent
                if u.color == 1:                          # if color of right child of grandparent i.e, uncle node is red
                    u.color = 0                           # Set color of childs as black
                    k.p.color = 0
                    k.p.p.color = 1                       # set color of grandparent as Red
                    k = k.p.p                             # Repeat algo on grandparent to remove conflicts
                else:
                    if k == k.p.right:                    # if k is right child of its parent
                        k = k.p
                        self.LR(k)                        # Call left rotate on parent of k
                    k.p.color = 0
                    k.p.p.color = 1
                    self.RR(k.p.p)                        # Call right rotate on grandparent
            if k == self.root:                            # If k reaches root then break
                break
        self.root.color = 0                               # Set color of root as black


    # Function to fix issues after deletion
    def fixDelete ( self , x ) :
        while x != self.root and x.color == 0 :           # Repeat until x reaches nodes and color of x is black
            if x == x.p.left :                            # If x is left child of its parent
                s = x.p.right                             # Sibling of x
                if s.color == 1 :                         # if sibling is red
                    s.color = 0                           # Set its color to black
                    x.p.color = 1                         # Make its parent red
                    self.LR ( x.p )                       # Call for left rotate on parent of x
                    s = x.p.right
                # If both the child are black
                if s.left.color == 0 and s.right.color == 0 :
                    s.color = 1                           # Set color of s as red
                    x = x.p
                else :
                    if s.right.color == 0 :               # If right child of s is black
                        s.left.color = 0                  # set left child of s as black
                        s.color = 1                       # set color of s as red
                        self.RR ( s )                     # call right rotation on x
                        s = x.p.right

                    s.color = x.p.color
                    x.p.color = 0                         # Set parent of x as black
                    s.right.color = 0
                    self.LR ( x.p )                       # call left rotation on parent of x
                    x = self.root
            else :                                        # If x is right child of its parent
                s = x.p.left                              # Sibling of x
                if s.color == 1 :                         # if sibling is red
                    s.color = 0                           # Set its color to black
                    x.p.color = 1                         # Make its parent red
                    self.RR ( x.p )                       # Call for right rotate on parent of x
                    s = x.p.left

                if s.right.color == 0 and s.right.color == 0 :
                    s.color = 1
                    x = x.p
                else :
                    if s.left.color == 0 :                # If left child of s is black
                        s.right.color = 0                 # set right child of s as black
                        s.color = 1
                        self.LR ( s )                     # call left rotation on x
                        s = x.p.left

                    s.color = x.p.color
                    x.p.color = 0
                    s.left.color = 0
                    self.RR ( x.p )
                    x = self.root
        x.color = 0


    # Function to transplant nodes
    def __rb_transplant ( self , u , v ) :
        if u.p == None :
            self.root = v
        elif u == u.p.left :
            u.p.left = v
        else :
            u.p.right = v
        v.p = u.p

    # Function to return node containing the given key
    def Tree_Search( self, k):
        x = self.root
        while x != self.NULL and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    # Function to return succesor of x
    def Tree_Successor(self, x):
        if x.right != self.NULL:
            return self.Tree_Minimum(x.right)
        y = x.p
        while y != self.NULL and x == y.right:
            x = y
            y = y.p
        return y

    # Function to return succesor of x
    def Tree_Predecessor(self, x):
        if x.left != self.NULL:
            return self.Tree_Maximum(x.left)
        y = x.p
        while y != self.NULL and x == y.left:
            x = y
            y = y.p
        return y

    # Function to handle deletion
    def delete_node_helper ( self , node , key ) :
        z = self.NULL
        while node != self.NULL :                          # Search for the node having that value/ key and store it in 'z'
            if node.key == key :
                z = node

            if node.key <= key :
                node = node.right
            else :
                node = node.left

        if z == self.NULL :                                # If Kwy is not present then deletion not possible so return
            print ( "Value not present in Tree !!" )
            return
        else:
            self.RB_Delete(z)

    def RB_Delete( self, z ):
        y = z
        y_original_color = y.color                          # Store the color of z- node
        if z.left == self.NULL :                            # If left child of z is NULL
            x = z.right                                     # Assign right child of z to x
            self.__rb_transplant ( z , z.right )            # Transplant Node to be deleted with x
        elif (z.right == self.NULL) :                       # If right child of z is NULL
            x = z.left                                      # Assign left child of z to x
            self.__rb_transplant ( z , z.left )             # Transplant Node to be deleted with x
        else :                                              # If z has both the child nodes
            y = self.Tree_Minimum ( z.right )                    # Find minimum of the right sub tree
            y_original_color = y.color                      # Store color of y
            x = y.right
            if y.p == z :                                   # If y is child of z
                x.p = y                                     # Set parent of x as y
            else :
                self.__rb_transplant ( y , y.right )
                y.right = z.right
                y.right.p = y

            self.__rb_transplant ( z , y )
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == 0 :                          # If color is black then fixing is needed
            self.fixDelete ( x )


    # Deletion of node
    def delete ( self , key ) :
        self.delete_node_helper ( self.root , key )         # Call for deletion


    # Function to print
    def __printCall ( self , node , indent , last ) :
        if node != self.NULL :
            print(indent, end=' ')
            if last :
                print ("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print ( str ( node.key ) + "(" + s_color + ")" )
            self.__printCall ( node.left , indent , False )
            self.__printCall ( node.right , indent , True )

    # Function to call print
    def print_RBTree ( self ) :
        self.__printCall ( self.root , "" , True )





import time
import random



rbt = RBTree()
a = list(map(int, input().split()))

st=time.process_time()
for k in a:
    x = RB_Node(k)
    rbt.RB_Insert(x)

et=time.process_time()
print(et-st)

def intro():
    pass
    # Red-Black Trees are a type of self-balancing binary search tree data structure that maintains balance during insertion and deletion operations.
    # Node Color: Each node is colored either red or black.
    # Root Property: The root is always black.
    # Red Property: Red nodes cannot have red children (i.e., no two consecutive red nodes in any path).
    # Black Depth Property: All paths from the root to any leaf must have the same number of black nodes (black depth).
    # Leaf Nodes: All leaf nodes (null or sentinel nodes) are considered black.
    # \

    # Insertion:

    # Insert the new node as you would in a regular binary search tree, but color it red.
    # Check and fix violations of the Red-Black properties by performing rotations and color changes.


    # Deletion:

    # Perform a regular binary search tree delete operation.
    # If the deleted node was red, there are no violations.
    # If the deleted node was black, the tree might become unbalanced. You need to perform additional operations to restore the Red-Black properties.

    # Rotations and color changes are the key operations that maintain the balance of the tree. 
    # There are four types of rotations: 
    #     left rotation
    #     right rotation
    #     left-right rotation (double rotation)
    #     right-left rotation (double rotation).
def function_explanation():
    pass
    '''
    
    RB_Node Class:
    This class defines the structure of a Red-Black Tree node.
    Each node has data (optional), a key (used for sorting), parent (p), left child (left), right child (right), and a color (1 for red, 0 for black).
    
    
    RBTree Class:
    This class represents the Red-Black Tree data structure.
    
    
    __init__(self):
    Constructor for the RBTree class.
    Initializes the NULL sentinel node with color 0 (black) and sets it as the root of the tree.
    
    
    insert(self, key):
    Public method to insert a new node with the given key into the Red-Black Tree.
    Creates a new node with the specified key and calls RB_Insert to insert it while maintaining the Red-Black properties.
    
    
    RB_Insert(self, node):
    Private method to insert a new node into the Red-Black Tree and fix any violations of the properties.
    Iteratively searches for the appropriate position to insert the new node and performs rotations and color adjustments as needed to maintain the Red-Black properties.
    
    
    Tree_Minimum(self, node), Tree_Maximum(self, node):
    Helper methods to find the minimum and maximum nodes, respectively, in the subtree rooted at the given node.
    
    
    LR(self, x), RR(self, x):
    Left and right rotation functions used to balance the tree during insertion and deletion.
    
    
    fixInsert(self, k):
    Fixes the tree properties after insertion of a node k.
    Performs necessary rotations and color adjustments to ensure that Red-Black properties are maintained.
    
    
    fixDelete(self, x):
    Fixes the tree properties after deletion of a node x.
    Performs rotations and color adjustments to rebalance the tree and maintain the Red-Black properties.
    
    
    __rb_transplant(self, u, v):
    Replaces subtree rooted at node u with subtree rooted at node v.
    Used during deletion to transplant subtrees.
    
    
    Tree_Search(self, k), Tree_Successor(self, x), Tree_Predecessor(self, x):
    Methods for searching a key, finding the successor, and finding the predecessor of a given node x.
    
    
    delete_node_helper(self, node, key), RB_Delete(self, z):
    delete_node_helper searches for the node with the specified key and calls RB_Delete to delete it.
    RB_Delete performs the actual deletion of the node z and fixes the tree properties.
    
    
    delete(self, key):
    Public method to delete a node with the given key from the Red-Black Tree.
    Calls delete_node_helper to locate and delete the node while maintaining Red-Black properties.
    
    
    __printCall(self, node, indent, last), print_RBTree(self):
    Functions for printing the Red-Black Tree with appropriate formatting.
    Recursively traverses the tree and prints each node's key and color.
    
    
    Main Block:
    Reads input integers, inserts them into the Red-Black Tree, and measures the time taken for insertion.'''


def four_case_explanation():
    pass
    # Case 1: Sibling is Red
    # Case 2: Sibling is Black and both of its children are Black
    # Case 3: Sibling is Black, its left child is Red, and its right child is Black
    # Case 4: Sibling is Black, and its right child is Red
    # Case 1: Sibling is Red
    # This case occurs when the sibling s of the deleted node x is red. To fix this case, we perform the following steps:

    # Set the color of s to black.
    # Set the color of x.p (parent of x) to red.
    # Perform a left rotation on x.p (parent of x).
    # Update s to be the new sibling of x.
    # After performing these steps, we have effectively converted Case 1 into one of the other cases.

    # Case 2: Sibling is Black and both of its children are Black
    # In this case, the sibling s of the deleted node x is black, and both of its children are also black. To fix this case, we perform the following steps:

    # Set the color of s to red.
    # Move up the tree by setting x to x.p (parent of x).
    # Now, we continue to fix the tree by checking the new color of x and its sibling s.

    # Case 3: Sibling is Black, its left child is Red, and its right child is Black
    # Here, the sibling s of the deleted node x is black, its left child is red, and its right child is black. To fix this case, we perform the following steps:

    # Set the color of s to red.
    # Set the color of s.left to black.
    # Perform a right rotation on s.
    # Update s to be the new sibling of x.
    # After these steps, the tree is transformed into Case 4, and we proceed to handle Case 4.

    # Case 4: Sibling is Black, and its right child is Red
    # In this final case, the sibling s of the deleted node x is black, and its right child is red. To fix this case, we perform the following steps:

    # Set the color of s to be the color of x.p (parent of x).
    # Set the color of x.p to black.
    # Set the color of s.right to black.
    # Perform a left rotation on x.p (parent of x).
    # Update x to be the root of the tree, as the fixing is complete.
    # After handling all these cases, the Red-Black Tree properties are restored, and the tree remains balanced.\
def insert():
    pass
    # The RB_Insert function is used to insert a new node into the Red-Black Tree while maintaining its properties.

    # It starts by initializing the new node node with color 1 (red), as the newly inserted node is always red according to Red-Black Tree rules.

    # It initializes variables y and x to None and the root node of the tree, respectively.

    # It enters a loop that traverses down the tree to find the appropriate position for the new node. 
    # It compares the key of the new node with the keys of the nodes in the tree and moves left or right accordingly until it finds an empty spot where the new node should be inserted.

    # Once the appropriate position is found, the parent p of the new node is set to y, and it is linked to the tree accordingly as a left or right child of y.

    # If the parent p of the new node is None, then the new node is the root of the tree, and its color is set to black, ensuring that the root node property is satisfied.

    # If the parent p of the new node's parent is None, it means that the parent of the new node is the root of the tree, and no further action is needed to maintain the Red-Black Tree properties.

    # If none of the above conditions are met, the fixInsert function is called to fix any violations of the Red-Black Tree properties that may have occurred due to the insertion.

    # The RB_Insert function ensures that the newly inserted node maintains the Red-Black Tree properties while properly positioning it within the tree.
    #  It sets the color of the new node initially to red, allowing any potential violations to be resolved in the subsequent call to the fixInsert function.
def fix_insert():
    pass
    # The function iterates while the color of the parent of k (the newly inserted node) is red, as this indicates a potential violation of the Red-Black Tree properties.

    # Inside the loop, it first checks whether the parent k.p is the right child of its parent k.p.p, which determines which subtree the uncle node u belongs to.

    # If the uncle node u is red, it means there is a conflict, and the function performs color changes to resolve the conflict:

    # Set the colors of the uncle u and the parent k.p to black.
    # Set the color of the grandparent k.p.p to red.
    # Move the focus up the tree to the grandparent k.p.p by assigning k to k.p.p.
    # If the uncle node u is black, the function handles two sub-cases:

    # If k is a left child of its parent k.p, perform a right rotation on the parent k.p to transform it into the right-child case.
    # Update the colors of the parent k.p and the grandparent k.p.p.
    # Perform a left rotation on the grandparent k.p.p to fix the tree structure.
    # Similar steps are performed if the parent k.p is a left child of its parent k.p.p, but the rotations are reversed.

    # The loop continues until k reaches the root node or until all conflicts are resolved.

    # After the loop, the function sets the color of the root node to black, ensuring that the root retains the property of being black.

    # The fixInsert function ensures that the Red-Black Tree properties are maintained after an insertion, specifically addressing violations related to consecutive red nodes and other potential conflicts.
def left_rotation():
    pass
    # The LR function is used to perform a left rotation around the node x in the Red-Black Tree.
    #  This rotation is used to balance the tree after insertion or deletion operations. 
    # Here's a detailed explanation of the steps:

    # The function begins by storing the right child of the node x in the variable y.

    # The right child of x is updated to be the left child of y.
    #  This step ensures that the tree structure is preserved.

    # If the left child of y is not the NULL sentinel node (indicating a real node),
    #  then the parent of that left child is updated to be x. 
    # This step adjusts the parent pointers of the nodes being rotated.

    # The parent of y is set to be the same as the parent of x, 
    # which maintains the parent-child relationships.

    # If the parent of x is None, it means x was the root node.
    #  In this case, we update the root of the tree to be y.

    # If x is the left child of its parent, the parent's left child pointer is updated to point to y.
    #  If x is the right child of its parent, the parent's right child pointer is updated to point to y. This step adjusts the parent's child pointers to point to the rotated subtree.

    # The left child of y is set to x, and the parent of x is updated to be y. 
    # This step completes the rotation, updating the left child and parent pointers of the rotated nodes.

    # After the left rotation is completed, 
    # the structure of the tree is adjusted such that the left child of x becomes the parent of x,
    #  and x becomes the left child of its previous right child. 
    # This helps maintain the balance and ordering properties of the Red-Black Tree.
def right_rotation():
    pass
    # The RR function is used to perform a right rotation around the node x in the Red-Black Tree.
    #  This rotation is similar to the left rotation but in the opposite direction. 
    # It helps maintain the balance and ordering properties of the Red-Black Tree.
    #  Here's a detailed explanation of the steps:

    # The function starts by storing the left child of the node x in the variable y.

    # The left child of x is updated to be the right child of y. 
    # This step preserves the tree structure.

    # If the right child of y is not the NULL sentinel node (indicating a real node),
    #  then the parent of that right child is updated to be x. 
    # This step adjusts the parent pointers of the nodes being rotated.

    # The parent of y is set to be the same as the parent of x, 
    # which maintains the parent-child relationships.

    # If the parent of x is None, it means x was the root node.
    #  In this case, we update the root of the tree to be y.

    # If x is the right child of its parent,
    #  the parent's right child pointer is updated to point to y.
    #  If x is the left child of its parent, the parent's left child pointer is updated to point to y.
    #  This step adjusts the parent's child pointers to point to the rotated subtree.

    # The right child of y is set to x, and the parent of x is updated to be y.
    #  This step completes the rotation, updating the right child and parent pointers of the rotated nodes.

    # After the right rotation is completed, the structure of the tree is adjusted such that the right child of x becomes the parent of x,
    #  and x becomes the right child of its previous left child.
    #  This helps maintain the balance and ordering properties of the Red-Black Tree.
def fixdelete():
    pass
    #     The function iterates while x is not the root node and the color of x is black. This loop is used to fix violations that might have been introduced after deleting a black node.

    # Inside the loop, it determines whether x is a left child or right child of its parent, and then calculates the sibling node s.

    # If the sibling s is red, it indicates a conflict, and the function performs color changes and rotations to resolve the conflict:

    # Set the color of the sibling s to black.
    # Set the color of the parent x.p to red.
    # Perform a left rotation on the parent x.p (if x is a left child of its parent) or a right rotation (if x is a right child of its parent) to transform the case into the sibling-black case.
    # Update the sibling s to the new sibling (which was previously a child of x.p).
    # If both children of the sibling s are black (or NULL sentinels), it sets the color of the sibling s to red, and the function moves up the tree by updating x to its parent x.p.

    # If one or both children of the sibling s are red, the function handles two sub-cases:

    # If the right child of s is black, it sets the color of the left child of s to black, sets the color of s to red, and performs a right rotation on s to transform it into the black-sibling-red-nephew case.
    # Update the sibling s to the new sibling (which was previously a child of x.p).
    # The function then updates the color of the sibling s to the color of the parent x.p and sets the color of the parent x.p to black.

    # The loop continues to process x up the tree until x reaches the root node or until all conflicts are resolved.

    # After the loop, the function sets the color of the node x (which might have been moved up the tree) to black, ensuring that the Red-Black Tree properties are maintained.

    # The fixDelete function ensures that the Red-Black Tree properties are maintained after a node deletion by addressing violations related to the removal of black nodes and performing necessary rotations to rebalance the tree.
def _rb_transplant():
    pass
    # The __rb_transplant method performs a subtree replacement operation within the Red-Black Tree. 
    # It replaces the subtree rooted at node u with the subtree rooted at node v. This operation involves updating the parent-child relationships to maintain the tree structure and properties after the replacement.

    # Here's a step-by-step breakdown of what the method does:

    # The method takes two arguments: u (the node to be replaced) and v (the node that will replace u).


    # The method starts by checking whether the parent of node u is None,
    #  which indicates that u is the root of the tree. If so, it updates the self.
    # root attribute to point to node v, effectively making v the new root of the tree.

    # If the parent of u is not None, the method checks whether u is the left child of its parent u.p. 
    # If it is, it updates the left attribute of u.p to point to node v, effectively making v the new left child of u.p.

    # If u is not the left child of its parent, it means it must be the right child, 
    # so the method updates the right attribute of u.p to point to node v, 
    # making v the new right child of u.p.

    # Finally, the method updates the parent attribute of node v to be the same as the parent attribute of node u. 
    # This ensures that the parent-child relationships are correctly maintained after the replacement.

    # By performing these updates, the __rb_transplant method effectively replaces the subtree rooted at node u with the subtree rooted at node v while maintaining the integrity of the Red-Black Tree structure and properties.
    #  This operation is crucial during node deletion, when a node with two children needs to be replaced with its successor or predecessor.
def delete__node__helper():
    pass
    #     Here's a detailed explanation of the steps taken in the delete_node_helper function:

    # The function takes two arguments: node (a starting node for the search) and key (the key to be deleted from the tree).

    # It initializes a variable z to self.NULL, which serves as a sentinel value indicating that the key to be deleted hasn't been found yet.

    # The function enters a loop that searches for the node with the specified key value. The loop continues until node becomes equal to the NULL sentinel (self.NULL), which indicates the end of the search.

    # Inside the loop, it checks whether the key of the current node matches the target key. If it does, the node z is assigned the value of the current node, indicating that the node with the desired key has been found.

    # Depending on the comparison between node.key and key, the function traverses either the left or right subtree of the current node to continue the search.

    # After exiting the loop, the function checks whether the value of z is still the NULL sentinel. If it is, it means the specified key was not found in the tree, and the function prints an error message and returns without performing any deletion.

    # If z is not the NULL sentinel, it means the node to be deleted has been found, and the function proceeds to call the RB_Delete method to remove the node from the Red-Black Tree.

    # The delete_node_helper function serves as an intermediary step to locate the node with the specified key and then delegates the deletion process to the RB_Delete method, which handles the actual removal of the node and maintenance of Red-Black Tree properties.
def rb_deletee():
    pass
    # Here's a detailed explanation of the steps taken in the RB_Delete function:

    # The function takes one argument, z, which is the node to be deleted from the Red-Black Tree.

    # It starts by assigning the value of z to the variable y. This is done to keep track of the node that will be effectively removed from the tree.

    # The color of the node y is stored in y_original_color to keep track of its original color.

    # The function then checks the cases of deleting a node with one child or two children:

    # If the left child of z is self.NULL (i.e., there's no left child), the function assigns the right child of z to the variable x. Then, it performs a transplant operation using the __rb_transplant method to remove z and replace it with its right child.
    # If the right child of z is self.NULL (i.e., there's no right child), the function assigns the left child of z to the variable x. Then, it performs a transplant operation using the __rb_transplant method to remove z and replace it with its left child.
    # If z has both left and right children, the function finds the minimum node (y) in the right sub-tree of z. It then updates x to y.right (which could be self.NULL), performs transplant operations to replace z with y, and updates the parent-child relationships accordingly.
    # After the deletion is complete, the function updates the y node to have the same properties as the original z node (key, data, color, etc.).

    # If the original color of node y (y_original_color) was black, it means that a black node was removed, and the function calls the fixDelete method to rebalance the tree and ensure Red-Black Tree properties are maintained.

    # The RB_Delete function performs the actual removal of a node from the Red-Black Tree and adjusts the tree structure as necessary to maintain its properties. It's a crucial part of the deletion process in a Red-Black Tree.
def delete():
    pass
    # The delete method initiates the process of deleting a node with a given key from the Red-Black Tree. 
    # It does so by calling the delete_node_helper method, which performs the actual deletion operation.

    # Here's a brief overview of what the delete method does:

    # It takes one argument: key, which is the key of the node to be deleted from the tree.

    # The method then calls the delete_node_helper method, passing in two arguments:

    # self.root: The starting point for the search for the node to be deleted (root of the tree).
    # key: The key of the node to be deleted.
    # The delete_node_helper method will search for the node with the specified key and handle the actual deletion process, including cases where the node has one or two children, as well as rebalancing the tree to maintain the Red-Black Tree properties.

    # By calling delete_node_helper, the delete method delegates the task of node deletion to the helper method, allowing for a clear and modular implementation of the deletion process in the Red-Black Tree.













