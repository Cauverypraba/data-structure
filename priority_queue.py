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
def poll():
    global size
    root = array[0]
    array[0] = array[size]
    size = size - 1    
    print('shiftdown')
    shiftDown(0)
    # return root                


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
            
# Function to remove elements from a heap
def remove(i):
    global size
    array.remove(i)
    size = size - 1
    shiftUp(i)
    # poll()
    return array
     

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
insert(7)
print('Priority Queue after inserting elements: ',array)
poll()
print("Priority Queue after polling highest priority element: ", end = ' ')
j = 0
print('size',size)
while (j <= size) :
    print(array[j], end = " ")
    j += 1 
print()       
getMax()
getMin()
changePriority(2, 49)
print("Priority Queue after changing the priority for a given element: ", end=' ')
k = 0
while (k <= size) :
    print(array[k], end = " ")
    k += 1
print()    
remove(11)
print("Priority Queue after removing an element: ", end=' ')
l = 0
while (l <= size) :
    print(array[l], end = " ")
    l += 1

