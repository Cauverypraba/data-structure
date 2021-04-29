'''Implementing Priority Queue using Binary Heap'''
array = [0]*50
size = -1

# Function to return parent of a given element
def parent(i):
    return (i - 1) // 2

# Function to return leftside element
def leftChild(i):
    return ((2 * i) + 1)

# Function to return rightside element
def rightChild(i):
    return ((2 * i) + 2)         

# Function to shiftUp the heap priority
def shiftUp(i):
    while (i > 0 and array[parent(i)] < array[i]) :
        # Swap parent and current node
        swap(parent(i), i)
        # Update i to parent of i
        i = parent(i)

# Function to shiftDown the heap priority
def shiftDown(i):
    maxIndex = i
    l = leftChild(i)
    if l <= size and array[l] > array[maxIndex]:
        maxIndex = l
    
    r = rightChild(i)
    if r <= size and array[r] > array[maxIndex]:
        maxIndex = r
    
    # If i is not same as maxIndex
    if i != maxIndex:
        swap(i, maxIndex)
        shiftDown(maxIndex)

# Function to insert element into heap with priority
def insert(p):
    global size
    size += 1
    array[size] = p
    shiftUp(size)

# Function to extract maximum element
def extractMax():
    global size
    i = 0
    max = array[0]
    while i < size:
        if array[i] > max:
            max = array[i]
        i += 1
    array.remove(max)
    size = size - 1    
    shiftDown(1)
    print("Priority Queue after extracting maximum element: ", array)                

# Function to extract minimum element
def extractMin():
    global size
    i = 0
    min = array[0]
    while i < size:
        if array[i] < min:
            min = array[i]
        i += 1
    array.remove(min)
    size = size - 1    
    shiftDown(1)
    print("Priority Queue after extracting minimum element: ", array)

#Function to get maximum element
def getMax():
    print(array[0])

#Function to get minimum element
def getMin():
    print(array[size])

# Function to change priority of an element
def changePriority(i, p):
    old_p = array[i]
    array[i] = p
    if old_p < p:
        shiftUp(i)
    else:
        shiftDown(i)
    print("Priority Queue after changing the priority for a given element: ", array)        

# Function to remove elements from a heap
def remove(i):
    global size
    array.remove(i)
    size -= 1
    shiftUp(i)
    print("Priority Queue after removing an element: ", array) 

# Function to swap elements
def swap(i, j) :  
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

insert(45)
insert(20)
insert(14)
insert(12)
insert(31)
insert(7)
insert(11)
insert(13)
insert(2)
# shiftDown(20)
extractMax()
# extractMin()
getMax()
# getMin()
changePriority(2, 49)
remove(14)
print(array)

