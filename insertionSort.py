array = [8, 5, 2, 9, 5, 6, 3]

# Time: O(n^2)      |       Space: O(1)
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        for j in reversed(range(1, i + 1)):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]


insertionSort(array)

print(array)

