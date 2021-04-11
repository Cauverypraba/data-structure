class Node():
    # Initialises a node object with data and its address
    def __init__(self, next = None, prev = None, data = None):
        self.data = data
        self.next = next
        self.prev = prev

# Class to perform doubly linked list functions using node object
class Doubly_List():
    # Function to initialise head
    def __init__(self, head):
        self.head = None

    # Function to insert data at beginning of the list
    def push(self, new_data):
        new_node = Node(data = new_data)

        # Point next of new_node as head
        new_node.next = self.head
        new_node.prev = None

        # Change prev of head node as newnode
        if self.head is not None:
            self.head.prev = new_node

        # Make new_node as head 
        self.head = new_node

    # Function to insert a new node at a particular position
    def insertAt(self, prev_node, new_data):
        # Check if the given prev_node exists  
        if prev_node is None:  
            print("The given previous node must be in LinkedList.")
            return
        # Create new node & put in the data  
        new_node = Node(data = new_data) 

        # Make next of new Node as next of prev_node  
        new_node.next = prev_node.next

        # Make next of prev_node as new_node  
        prev_node.next = new_node

        # Make prev node as previous of new node
        new_node.prev = prev_node

        # Change previous of new_node's next node 
        if new_node.next is not None:
            new_node.next.prev = new_node          
    
    #Function to insert element at the end of a list
    def append(self, new_data):
        new_node = Node(data = new_data)
        node = self.head
        if self.head == None:
            self.head = new_node
            return
        while(node.next):
            # print('inside', node.data)
            node = node.next
        node.next = new_node
        node = new_node.prev    
    
    # Function to delete a node
    def deleteNode(self,key):
        temp = self.head
        # check key to be deleted is a head node
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
        # Traverse list until key matches the data in list               
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None 

    # Function to print the list
    def printList(self, node):
        while(node):
            print(node.data)
            node = node.next

obj = Doubly_List(7)
obj.push(5)
obj.push(16)
obj.push(8)
obj.append(19)
obj.deleteNode(19)
obj.push(27)
obj.insertAt(obj.head.next, 4)
obj.printList(obj.head)
# print(obj.head.next.data)
