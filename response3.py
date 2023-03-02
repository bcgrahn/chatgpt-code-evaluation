

class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
# A function to do inorder tree traversal 
def inorder(root): 
  
    if root is not None: 
        inorder(root.left) 
        print(root.data) 
        inorder(root.right) 
  
# A function to insert a new node in the binary search tree 
def insert( node, data): 
  
    # If the tree is empty, return a new node 
    if node is None: 
        return Node(data) 
  
    else: 
        # Otherwise, recur down the tree 
        if data <= node.data: 
            node.left = insert(node.left, data) 
        else: 
            node.right = insert(node.right, data) 
  
        # return the (unchanged) node pointer 
        return node 
  
# Driver program to test the above functions 
# Let us create the following BST 
#      50 
#    /      \ 
#   30     70 
#   / \    / \ 
#  20 40  60 80 
root = None
root = insert(root, 50) 
insert(root, 30) 
insert(root, 20) 
insert(root, 40) 
insert(root, 70) 
insert(root, 60) 
insert(root, 80) 
  
# Print inoder traversal of the BST 
inorder(root)