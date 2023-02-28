array = [8, 5, 2, 9, 5, 6, 3]

# Time: O(nlogn)    |   Space: O(nlogn)
def mergeSort(array):
    if len(array) == 1:
        return array
    midIdx = len(array) // 2 
    leftArray = array[:midIdx]
    rightArray = array[midIdx:]
    return mergeIndividuallySortedArrays(mergeSort(leftArray), mergeSort(rightArray)) 

def mergeIndividuallySortedArrays(leftArray, rightArray):
    combinedArray = []
    i = j = 0
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] <= rightArray[j]:
            combinedArray.append(leftArray[i])
            i += 1
        else:
            combinedArray.append(rightArray[j])
            j += 1

    if i < len(leftArray):
        combinedArray.extend(leftArray[i:])
    elif j < len(rightArray):
        combinedArray.extend(rightArray[j:])

    return combinedArray 
    
print(mergeSort(array))