class Stack2():
    class Node():
        def __init__(self, value, next):
            self.value = value
            self.next = None
    def __init__(self):
        self.head = None
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
        print("Peek element: ",self.head.value)

    # To insert value into stack
    def push(self, value):
        self.head = self.Node(value, self.head)
        self.size += 1        
    
    # To remove value from stack
    def pop(self, key):
        if self.isEmpty():
            raise Exception("Cannot pop from a empty stack..")
        result = self.head.value
        self.head = self.head.next
        print(result)    

    def printStack(self):
        temp = self.head
        # print(temp.value)
        stack = [] 
        while(temp):
            print(temp.value)
            stack.append(temp.value)
            temp = temp.next
            # print(temp.value)
        print("Stack: ",stack[::-1])      
           
st = Stack2()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.peek()
st.pop(4)
st.printStack()           