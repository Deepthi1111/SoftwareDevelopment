array = [8, 5, 2, 9, 5, 6, 3]

# Time: O(nlog(n))     |    Space: O(log(n))
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)    

def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    pivot = startIdx 
    left = startIdx + 1
    right = endIdx

    while left <= right:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            array[left], array[right] = array[right], array[left]
        elif array[left] <= array[pivot]:
            left += 1           
        elif array[right] >= array[pivot]:
            right -= 1
           
    array[pivot], array[right] = array[right], array[pivot]

    leftSubArrayLength = right - 1 - startIdx
    rightSubArrayLength = endIdx - (right + 1)

    if leftSubArrayLength <= rightSubArrayLength:
        quickSortHelper(array, startIdx, right - 1)
        quickSortHelper(array, right + 1, endIdx)
    else:
        quickSortHelper(array, right + 1, endIdx)
        quickSortHelper(array, startIdx, right - 1)

quickSort(array)
print(array)        

