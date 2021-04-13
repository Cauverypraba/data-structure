'''Bubble Sort Algorithm using Python.'''
def bubbleSort(array):
    j = 0
    length = len(array)
    for i in range(0, length-1):
        if i < length-1 and array[i] > array[i+1]:
            array[i],array[i+1] = array[i+1],array[i]
            j += 1
            # print(array)
    length = j
    print(array)    

array = [-2, 45, 0, 11, -9] 
bubbleSort(array)           