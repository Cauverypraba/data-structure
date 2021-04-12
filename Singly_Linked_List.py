class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Linked_List():
    def __init__(self):
        self.head = None

    # Function to insert new data at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        # Point next of new_node as head
        new_node.next = self.head
        # Make new_node as head 
        self.head = new_node

    # Function to insert a new node after a given previous node
    def insertAt(self, prev_node, new_data):
        # Check if the given prev_node exists  
        if prev_node is None:  
            print("The given previous node must inLinkedList.")
            return
        # Create new node & put in the data  
        new_node = Node(new_data)  
        # Make next of new Node as next of prev_node  
        new_node.next = prev_node.next
        # Make next of prev_node as new_node  
        prev_node.next = new_node   

    # To insert new node at the end
    def append(self, new_data): 
        # Create a new node and put in the data then set next as None 
        new_node = Node(new_data) 
        # If the Linked List is empty, then make the new node as head 
        if self.head is None: 
                self.head = new_node 
                return
        # Else traverse till the last node 
        last = self.head 
        while (last.next): 
            last = last.next
        # Change the next of last node 
        last.next =  new_node 

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
            print('inside')
            return
        prev.next = temp.next
        temp = None    
    
    def printList(self): 
        temp = self.head
        nodes = []
        while (temp): 
            nodes.append(temp.data)
            print (temp.data) 
            print(nodes)
            temp = temp.next
        nodes.append('None')
        print(nodes)    

li = Linked_List()
li.push(5)
li.push(9)
li.push(2)
li.insertAt(li.head.next,7)
li.append(12)
li.deleteNode(7)
li.append(10)
li.printList()
