'''Implementing a Stack using Singly Linked List.'''
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack():
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # To get the size of stack
    def getSize(self):
        return self.size

    # To check whether the stack is empty
    def isEmpty(self):
        return self.size == 0            
    
    # To get top value from the stack
    def peek(self):
        if self.isEmpty():
            raise Exception("Cannot peek from a empty stack..")
        print("Peek element: ",self.head.next.value)

    # To insert value into stack
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1        
    
    # To remove value from stack
    def pop(self, key):
        temp = self.head.next
        if temp.value == key:
            self.head.next = temp.next
            temp = None    
        while(temp):
            if temp == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None
        self.size -= 1    

    def printStack(self):
        temp = self.head.next
        # print(temp.value)
        stack = [] 
        while(temp):
            print(temp.value)
            stack.append(temp.value)
            temp = temp.next
            # print(temp.value)
        print("Stack: ",stack[::-1])    

st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.peek()
st.pop(4)
st.printStack()
