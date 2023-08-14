import sys
sys.setrecursionlimit(10001)

root = None
        

class node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.p = None    #parent
        self.left = None
        self.right = None


def Inorder_Tree_Walk(x):
    if x != None:
        Inorder_Tree_Walk(x.left)
        print(x.key)
        Inorder_Tree_Walk(x.right)


def Tree_Minimum(x):
    
    # Replace "pass" with your code
    while x.left!=None:
        x=x.left
    return x
    

def Tree_Maximum(x):
    # Replace "pass" with your code
    while x.right!=None:
        x=x.right
    return x

def Tree_Successor(x):
    # Replace "pass" with your code
    # pass
    if x.right!=None:
        return Tree_Minimum(x.right)
    y=x.p
    while y!= None and x==y.right:
        x=y
        y=y.p
    return y

'''
Adding your own Tree_Predecessor(x) is recommended, but not required
'''

def Transplant(u, v):
    # This function is required for supporting Tree_Delete
    # Replace "pass" with your code
    # pass
    global root

    if u.p==None:
        root=v
    elif u==u.p.left:
        u.p.left=v
    else:
        u.p.right=v
        if v!=None:
            v.p=u.p

def Tree_Delete(z):
    # Replace "pass" with your code
    # pass  
    if z.left==None:
        Transplant(z,z.right)
    elif z.right==None:
        Transplant(z,z.left)
    
    else:
        y=Tree_Minimum(z.right)
        if y.p!=z:
            Transplant(y,y.right)
            y.right=z.right
            y.right.p=y
        Transplant(z,y)
        y.left=z.left



def Tree_Search(x,k):
    global root
    if x==None or k==x.key:
        return x
    if k<x.key:
        return Tree_Search(x.left,k)
    else:
        return Tree_Search(x.right,k)

    # Replace "pass" with your code
    # pass
def Tree_Insert(key, data):
    global root
    
    new_node = node(key, data)
    y = None
    x = root
    while x != None:
        y = x
        if new_node.key < x.key:
            x = x.left
        else:
            x = x.right
    new_node.p = y
    if y == None:
        root = new_node
    elif new_node.key < y.key:
        y.left = new_node
    else:
        y.right = new_node

    
    

# Function to print
def printCall ( node , indent , last ) :
    if node != None :
        print(indent, end=' ')
        if last :
            print ("R----",end= ' ')
            indent += "     "
        else :
            print("L----",end=' ')
            indent += "|    "

        print ( str ( node.key ) )
        printCall ( node.left , indent , False )
        printCall ( node.right , indent , True )

# Function to call print
def print_BSTree (root) :
    printCall( root , "" , True )

Tree_Insert(33, "Data for node 33")
Tree_Insert(44, "Data for node 44")
Tree_Insert(12, "Data for node 12")
Tree_Insert(44, "Data for node 44")  # This will insert a new node with the same key as an existing node
Tree_Insert(33, "Data for node 33")  # This will insert a new node with the same key as an existing node
Tree_Insert(32, "Data for node 32")

# Print the binary search tree
print_BSTree(root)

max_node = Tree_Maximum(root)

if max_node is not None:
    print(f"Maximum Node: Key={max_node.key}, Data={max_node.data}")
else:
    print("The tree is empty. No maximum node.")
