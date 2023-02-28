array = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
]

source = 3 

# Time: O(n^2)      |       Space: O(n^2)
def waterfallStreams(array, source):
    fountain = array[:]
    fountain[0][source] = -1
    for rowIdx in range(1, len(fountain)):  
        prevRowIdx = rowIdx - 1     
        for colIdx in range(len(fountain[0])):
            if fountain[prevRowIdx][colIdx] == 1:
                continue
            if fountain[prevRowIdx][colIdx] < 0 and fountain[rowIdx][colIdx] <= 0:
                fountain[rowIdx][colIdx] += fountain[prevRowIdx][colIdx]
                continue
            if fountain[prevRowIdx][colIdx] < 0 and fountain[rowIdx][colIdx] == 1:
                splitWater = fountain[prevRowIdx][colIdx] / 2
                leftIdx = rightIdx = colIdx
                while leftIdx - 1 >= 0: 
                    if fountain[rowIdx][leftIdx] ==  1:
                        leftIdx -= 1
                        continue           
                    if fountain[rowIdx][leftIdx] <= 0:
                        fountain[rowIdx][leftIdx] += splitWater
                        break                     
                while rightIdx + 1 < len(fountain[rowIdx]):                    
                    if fountain[rowIdx][rightIdx] == 1:
                        rightIdx += 1
                        continue
                    if fountain[rowIdx][rightIdx] <= 0:
                        fountain[rowIdx][rightIdx] += splitWater
                        break  
    return list(map(lambda x: x * (-100), fountain[-1]))

            



    

print(waterfallStreams(array, source))


        
        






