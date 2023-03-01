def nonAttackingQueens(n):
    columnPlacements = [0] * n 
    return getNumberOfValidWaysOfQueenPlacements(0, columnPlacements, n)

def getNumberOfValidWaysOfQueenPlacements(row, columnPlacements, boardSize):
    if row == boardSize:
        return 1 
    validPlacements = 0
    for col in range(boardSize):
        if isPathClearForQueen(row, col, columnPlacements):
            columnPlacements[row] = col
            validPlacements += getNumberOfValidWaysOfQueenPlacements(row + 1, columnPlacements, boardSize)

    return validPlacements

def isPathClearForQueen(row, col, columnPlacements):
    for previousRow in range(row):
        prevColumn = columnPlacements[previousRow]
        isColumnTaken = prevColumn == col 
        isDiagonalTaken = abs(prevColumn - col) == row - previousRow
        if isColumnTaken or isDiagonalTaken:
            return False 
    return True

print(nonAttackingQueens(4))