array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]

# Time: O(n)        |       Space: O(1)
def threeNumberSort(array, order):
    firstOrderIdx = 0
    lastOrderIdx = len(array) - 1    

    for idx in range(len(array)):
        if array[idx] == order[0]:
            array[idx], array[firstOrderIdx] = array[firstOrderIdx], array[idx]  
            firstOrderIdx += 1

    for idx in reversed(range(firstOrderIdx, len(array))):
        if array[idx] == order[2]:
            array[idx], array[lastOrderIdx] = array[lastOrderIdx], array[idx]
            lastOrderIdx -= 1
    
threeNumberSort(array, order)

print(array)
        


    