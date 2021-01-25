class Linked_List():
    def __init__(self):
        self.data = [5]
        self.next = None
        self.head = None

    def insert(self, data):
        if self.data == None:
            self.next = None
            self.head = self.data
        self.next = self.head
        self.head = self.data
        return data

li = Linked_List()
li.insert(5)        