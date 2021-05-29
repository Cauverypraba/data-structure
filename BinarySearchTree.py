class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def search(root, key):
    if root is None or root.val == key:
        return root
    else:
        if  key > root.val:
            return search(root.right, key)
    return search(root.left, key)


def insertElement(root, key):
    if root is None:
        return Node(key)
    else:    
        if root.val == key:
            return root    
        elif root.val < key:
            root.right = insertElement(root.right, key)
            # root.right = key
            # print('...', root.right)
        else:
            root.left = insertElement(root.left, key)
            # root.left = key
            # print('//', root.left)
    print(root.val)        
    return root

def inorder(root):
    if root:
        print('==',root.val)
        # print(root.left)
        inorder(root.left)
        print('val',root.val)
        inorder(root.right)

r = Node(50)
r = insertElement(r, 30)
r = insertElement(r, 20)
r = insertElement(r, 40)
r = insertElement(r, 70)
r = insertElement(r, 60)
r = insertElement(r, 80)            
inorder(r)
print('r',r.val)

