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
    # print('___',i)
    while (i > 0 and array[parent(i)] < array[i]) :
        print('inside')
        # Swap parent and current node
        swap(parent(i), i)
        # print('###',parent(i), i)
        # Update i to parent of i
        i = parent(i)
        # print('ii', i)
        # print(array)

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
# def insert(p):
#     global size
#     size += 1
#     array[size] = p
#     shiftUp(size)
#     print('p',p)

# # Function to extract maximum element
# def extractMax():
#     global size
#     i = 0
#     max = array[0]
#     while i < size:
#         if array[i] > max:
#             max = array[i]
#         i += 1
#     array.remove(max)
#     size = size - 1    
#     shiftDown(1)        
    # result = array[0]   
    # Replace the value 
    # at the root with 
    # the last leaf
    # array[0] = array[size]
    # size = size - 1
       
    # Shift down the replaced 
    # element to maintain the 
    # heap property
    # shiftDown(0)
    # return result
    # print(array)        

# Function to get maximum element
# def getMax():


def swap(i, j) :  
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

insert(45)
insert(43)
insert(14)
insert(12)
insert(31)
insert(7)
insert(11)
insert(13)
insert(7)
# shiftDown(20)
extractMax()
print(array)

