array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7],
]

# Time: O(n)    |       Space: O(n)
def spiralTraverse(array):
    spiralOrderArray = []
    startRow = 0
    startCol = 0
    endRow = len(array) - 1
    endCol = len(array[0]) - 1

    while startRow < endRow and startCol < endCol:
        for col in range(startCol, endCol + 1):
            spiralOrderArray.append(array[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            spiralOrderArray.append(array[row][endCol])

        for col in reversed(range(startCol, endCol)):
            spiralOrderArray.append(array[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            spiralOrderArray.append(array[row][startCol])

        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1

    return spiralOrderArray 

print(spiralTraverse(array))
