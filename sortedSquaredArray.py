array = [-4, -3, -2, -1, 0, 5, 6, 7]

# Time: O(n)    |       Space: O(n)
def getSortedSquaredArray(array):
    sortedSquaredArray = [None] * len(array)
    nextIdx = j =len(array) - 1
    i = 0

    while nextIdx >= 0:
        if abs(array[i]) >= abs(array[j]):
            sortedSquaredArray[nextIdx] = array[i] * array[i]          
            i += 1
        else:
            sortedSquaredArray[nextIdx] = array[j]*array[j]
            j -= 1
        nextIdx -= 1
    return sortedSquaredArray

print(getSortedSquaredArray(array))
            