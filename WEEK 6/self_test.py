import sys
sys.setrecursionlimit(10000)



# Step 1: Define the Node class
# Start by defining the Node class to represent individual nodes in the binary search tree.
#  Each node should have a key, left child, and right child.

class node:
    def __init__(self,key,data):
        self.key=key
        self.data=data
        self.p=None
        self.left=None
        self.right=None

class Tree:
    def __init__(self,root=None):
        self.root=None
    def insert(self,  key_to_insert,data):
        new_node=node(key_to_insert,data)
        
        y=None
        x= self.root
            

        while x!=None:
            y=x
                
            if new_node.key<x.key:
                x=x.left
            else:
                x=x.right
        new_node.p=y
        if y==None:
            self.root=new_node
        elif new_node.key<y.key:
            y.left=new_node
        else:
            y.right=new_node
    def search(self,key):
        x=self.root
        while x!=None and key!=x.key:
            if key<x.key:
                x=x.left
            else :
                x=x.right
        return x
     

    def transplant(self,u,v):
        if u.p ==None:
            self.root=v    # u become node
            
        elif u==u.p.left:  #if u is one the left
            u.p.left=v
        else:              #if u is on the right
            u.p.right=v

        if v!=None: # in case o not delete (v is a node)
            v.p=u.p
    


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
tree=Tree()
keys_to_insert = [56, 70, 30, 60, 65, 22, 11, 16, 40, 95, 63, 3, 67]
for key in keys_to_insert:
    tree.insert (key,data=None)
tree.delete(40)
print_BSTree(tree.root)