array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]

# Time: O(n^2)      |        Space: O(n)
def minNumOfJumps(array):

    numOfJumps = [float("inf") for num in array]
    numOfJumps[0] = 0
    for i in range(1, len(array)):
        for j in range(i):
            if j + array[j] >= i:
                jump = numOfJumps[j] + 1
                numOfJumps[i] = min(numOfJumps[i], jump)
    return numOfJumps[-1]

print(minNumOfJumps(array))
