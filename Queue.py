'''Implementation of Queue using Singly Linked List '''
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None

    def enqueue(self, value):
        node = Node(value)
        if self.tail == None:
            self.head = self.tail = node
            print('inside')
        self.tail.next = node
        self.tail = node

    def dequeue(self):
        if self.isEmpty():
            return
        temp = self.head
        self.head = temp.next
    
    def printQueue(self):
        temp = self.head
        # print(temp.value)
        queue = [] 
        while(temp):
            # print(temp.value)
            queue.append(temp.value)
            temp = temp.next
            # print(temp.value)
        print("Queue:",queue)

if __name__== '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(8)
    q.enqueue(28)
    q.enqueue(32)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.printQueue()        


