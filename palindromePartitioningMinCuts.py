string = "noonabbad"

# Time: O(n^2)      |       Space: O(n^2)
def palindromePartitioningMinCuts(string):
    palindromicity = [[None for j in range(len(string))] for i in range(len(string))]
    minCutsSoFar = [float("inf") for letter in string]

    for i in range(len(string)):
        for j in range(i, len(string)):
            palindromicity[i][j] = isPalindrome(string, i, j)
    
    minCutsSoFar[0] = 0

    for idx in range(1, len(minCutsSoFar)):
        if palindromicity[0][idx] == True:
            minCutsSoFar[idx] = 0
            continue 
        else:
            minCutsSoFar[idx] = min(minCutsSoFar[idx-1] + 1, minCutsSoFar[idx])
            currentPalindromicityColumn = list(map(lambda row: row[idx], palindromicity))
            for boolIdx in reversed(range(1, idx)):
                if palindromicity[boolIdx][idx] == True:
                    minCutsSoFar[idx] = min(minCutsSoFar[boolIdx - 1] + 1, minCutsSoFar[idx])
    
    return minCutsSoFar[-1]

def isPalindrome(string, startIdx, endIdx):
    while startIdx < endIdx:
        if string[startIdx] is not string[endIdx]:
            return False 
        startIdx += 1
        endIdx -= 1 
    return True 


print(palindromePartitioningMinCuts(string))

