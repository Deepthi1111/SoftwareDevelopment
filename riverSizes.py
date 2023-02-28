"""You're given a two dimentional array(a matrix) of potentially unequal height and width containing only 0s and 1s.
Each 0 represents land and each 1 represents a part of a river. A river consists of any number of 1s that are either horizontally
or vertically adjacent(but not diagonally adjacent). The number of adjacent 1s forming a river determine its size.

Note that a river can twist, in other words, it doesnt have to be a straight vertical line or a straight horizontal line;
It can be L shaped for example.

Write a function that returns an array of the sizes of all rivers represented in the input matrix.
The sizes dont need to be in any particular order. """


"""
1) Create a empty output array to hold the riverSizes. The length of this array will indicate the number of rivers.
2) Have an addtional 2D array, isVisited which will hold the boolean values to tell if this location(coordinates in the map)
    is already visited.
3) Walk through the given map row by row (like days in a calendar).
4) For each postition on the map check if this location is already visited.
5) If not visited (mark the isVisited to True) and look at the value contained in map, if its 0,
    There is no river, therefore no need to count any river size, Try next location.
6) If it is 1 , make currentRiverSize to += 1 and look for next locations to visit.
7) Next locations to see where the river is flowing will be Up, down, left and right.
 We will check if there is place to move and then move(Dont want to go outside the bounds of the array)
"""
matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
 ]
def getRiverSizes(matrix):
    riverSizes = []
    isVisited = [[False for value in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if isVisited[i][j]:
                continue
            if matrix[i][j] == 0:
                isVisited[i][j] = True
                continue
            # When visitThePosition gets called, that will be the starting point of a river.
            riverSizes = visitThePosition(i, j, matrix, isVisited, riverSizes)
    return riverSizes

from collections import deque
def visitThePosition(i, j, matrix, isVisited, riverSizes):
    positionsToExplore = deque([[i,j]]) # We are going to store list of coordinates. So 2D array.
    currentRiverSize = 0
    while len(positionsToExplore):
        currentPostion = positionsToExplore.popleft()
        x, y = currentPostion
        isVisited[x][y] = True
        if matrix[x][y] == 0: # We are checking the matrix[x][y] because this which loop is going to run for all the surrounding positions.
            isVisited[x][y] = True
            continue
        currentRiverSize += 1
        nextPositions = searchNearby(x, y, isVisited)
        positionsToExplore.extend(nextPositions)
        # for pos in nextPostions:
        #     positionsToExplore.append(pos)
    if currentRiverSize > 0:
            riverSizes.append(currentRiverSize)
    return riverSizes

"""
            [i-1, j]
[i, j-1]    [i, j]        [i, j+1]
            [i+1, j]
"""

def searchNearby(i, j, isVisited):
    nextPositionsToExplore = []
    if i > 0 and not isVisited[i-1][j]:                 #LEFT
        nextPositionsToExplore.append([i-1, j])
    if i < len(isVisited) - 1 and not isVisited[i+1][j]: #RIGHT
        nextPositionsToExplore.append([i+1, j])
    if j > 0 and not isVisited[i][j-1]:                  #UP
        nextPositionsToExplore.append([i, j-1])
    if j < len(isVisited[0]) - 1 and not isVisited[i][j+1]: #DOWN
        nextPositionsToExplore.append([i, j+1])
    return nextPositionsToExplore

print(getRiverSizes(matrix))
