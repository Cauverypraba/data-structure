class Dynamic():
    """ Dynamic Array implementation """
    def __init__(self):
        self.capacity = 1
        self.dynamic_array = [0] * self.capacity
        self.substitute_array = []
        self.array_length = 0
        
    def len(self):
        """
        Method to get the length of array 
        returns: int
        """
        return self.array_length
    
    def getItem(self, element):
        """
        Method to get particular item from an array
        param: element: int
        returns: int
        """
        if not 0 <= element <self.array_length:
            return IndexError('Element is out of bound')
        return self.dynamic_array[element]    
    
    def append(self, element):
        """
        Method to add element at last of an array, 
        if length is greater than capacity calls resize() to increase the length
        param: element: int
        returns: list
        """
        if self.array_length == self.capacity: 
            self.resize(2 * self.capacity)
        self.dynamic_array[self.array_length] = element
        self.array_length += 1
        return self.dynamic_array        
    
    def insertAt(self, index, element):
        """
        Method to insert element at particular index
        params: index, element: int, int
        returns: list
        """
        if self.array_length == self.capacity:    
            self.resize(2 * self.capacity)
        self.dynamic_array[index] = element
        self.array_length += 1
        return self.dynamic_array

    def remove(self, index):
        """
        Method to remove element in an array
        param: index: int
        returns: array
        """
        if self.array_length > self.capacity:
            print("Only elements within the range can be deleted")
        self.dynamic_array.pop(index)
        return self.dynamic_array       

    def resize(self, new_cap):
        """
        Method to increase the size of array 
        """
        self.substitute_array = [0] * new_cap
        for iter in range(self.array_length):  
            self.substitute_array[iter] = self.dynamic_array[iter] 
             
        self.dynamic_array = self.substitute_array
        self.capacity = new_cap
    
if __name__ == '__main__':    
    obj = Dynamic()
    obj.append(13)
    obj.append(22)
    obj.append(6)
    obj.append(18)
    obj.insertAt(7,20)
    obj.remove(7)
