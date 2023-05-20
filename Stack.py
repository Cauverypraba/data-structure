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
        print("Peek element: ", self.head.next.value)

    # To insert value into stack
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1        
    
    # To remove value from stack
    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot pop from a empty stack..")
        temp = self.head.next
        self.head.next = temp.next
        temp = None
        self.size -= 1    

    def printStack(self):
        temp = self.head.next
        stack = [] 
        while(temp):
            stack.append(temp.value)
            temp = temp.next
        print("Stack: ",stack)    

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.peek()
    stack.pop()
    stack.pop()
    stack.printStack()
