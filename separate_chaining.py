class Node:
    """
    Class to create Node with key and value
    """
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None

class SeparateChain:
    """
    Class to perform hash functionality
    """
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.size = 0
        self.hash_table = [None] * capacity

    def _hash_value(self, key):
        """
        Return index for a key
        """
        return hash(key) % self.capacity

    def insert(self, key, value):
        """
        Insert a key in a hash table
        """
        index = self._hash_value(key)
        # Assign key to index if its None
        if self.hash_table[index] is None:
            self.hash_table[index] = Node(key, value)
        else:
            current = self.hash_table[index]
            # Iterates until last node
            while current.next:
                current = current.next
            current.next = Node(key, value)

def display_table(hash_table):
    """
    Print hash table with keys and values
    """
    for index, node in enumerate(hash_table.hash_table):
        print(f"Index {index}: ", end="")
        while node:
            print(f"({node.key}: {node.value})", end=" -> ")
            node = node.next
        print("None")


hash_instance = SeparateChain(capacity=8)
hash_instance.insert(8, "Apple")
hash_instance.insert(30, "Mango")
hash_instance.insert(30, "Pine Apple")
hash_instance.insert(20, "Strawberry")
hash_instance.insert(9, "Orange")
hash_instance.insert(20, "Banana")
display_table(hash_instance)
