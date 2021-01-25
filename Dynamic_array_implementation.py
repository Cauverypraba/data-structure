class Dynamic():
    def __init__(self):
        self.capacity = 1
        self.A = [0] * self.capacity
        self.B = []
        self.n = 0
        
    def len(self):
        return self.n
    
    def getItem(self, i):
        if not 0 <= i <self.n:
            return IndexError('i is out of bound')
        return self.A[i]    
    
    def append(self, num):
        # print(self.n)
        # print(len(self.A))
        if self.n == self.capacity:
            self.capacity = 2 * self.capacity
            print(self.n, self.capacity)
            self.B = [0] * self.capacity
            for i in range(0, len(self.A)):
                self.B[i] = self.A[i]
                print(self.B)
            self.A = [0] * self.capacity    
            for i in range(0, len(self.B)):
                self.A[i] = self.B[i]      
            #print(self.B)
            #print('#',type(self.A))
        self.A[self.n] = num
        self.n += 1
        return self.A        
    
    def insertAt(self, z, num):
        n = len(self.A)
        if self.n == self.capacity:
            self.capacity = 2 * self.capacity
            print(self.n, self.capacity)
            self.B = [0] * self.capacity
            for i in range(0, len(self.A)):
                self.B[i] = self.A[i]
                print(self.B)
            self.A = [0] * self.capacity    
            for i in range(0, len(self.B)):
                self.A[i] = self.B[i]
        # print(self.A[self.n])    
        self.A[z] = num
        #self.n += 1
        return self.A

    def remove(self, n):
        if self.n > self.capacity:
            print("Only elements within the range can be deleted")
        self.A.pop(n)
        return self.A        
obj = Dynamic()
print(obj.append(13))
print(obj.append(22))
print(obj.append(6))
print(obj.append(18))
print(obj.insertAt(7,20))
print(obj.remove(7))
#print(obj.insertAt(0,25),'insertAt')
