class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def search(root, key):
    if root is None or root.val == key:
        return root
    else:
        if key > root.val:
            return search(root.right, key)
    return search(root.left, key)

# Function to do inorder traversal of BST.
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# Function to do preorder traversal of BST.
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

# Function to do postorder traversal of BST.
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

# Function to insert a new node in BST.
def insertElement(root, key):
    if root is None:
        return Node(key)
    else:    
        if root.val == key:
            return root    
        elif root.val < key:
            root.right = insertElement(root.right, key)
        else:
            root.left = insertElement(root.left, key)        
    return root

# This function returns the min key value of a node, 
# instead of searching an entire tree.
def minValueNode(node):
    curr = node
    while curr.left is not None:
        curr = node.left
    return curr    

# Function that removes a node from Binary Search Tree and returns a new root.
def deleteNode(root, key):
    if root is None:
        return root    
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    # If key is same as root's key, then this is the node
    # to be deleted    
    else:
        # Node with only one child or no child
        if root.left == None:
            temp = root.right
            root = None
            return temp
        elif root.right == None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)    
        temp = minValueNode(root.right)
        
        # Copy the inorder successor's
        # content to this node
        root.val = temp.val  
        
        # Delete the inorder successor
        root.right = deleteNode(root.right, key)   
    return root            
        

r = Node(50)
r = insertElement(r, 30)
r = insertElement(r, 20)
r = insertElement(r, 40)
r = insertElement(r, 70)
r = insertElement(r, 60)
r = insertElement(r, 80)

print('Inorder Traversal of BST')
inorder(r)
print('Preorder Traversal of BST')
preorder(r)
print('Postorder Traversal of BST')
postorder(r)

print("\nDelete 20")
r = deleteNode(r, 20)

print("Inorder traversal of the modified tree")
inorder(r)


