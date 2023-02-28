"""
Bubble sort is an algorithm where the biggest number bubbles up to the end of the array after each iteration.
"""


array = [8, 5, 2, 9, 5, 6, 3]


# Time: O(n^2)      |       Space: O(1)
def bubbleSort(array):
    counter = 0
    isSwapPerformed = True
    while isSwapPerformed:
        isSwapPerformed = False
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSwapPerformed = True 
        counter += 1 
    
bubbleSort(array)

print(array)




