array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

# Time: O(n) |  Space: O(1)
def validateSubsequence(array, sequence):
    j = 0 
    for i in range(len(array)):
        if array[i] == sequence[j]:
            j += 1
        if j == len(sequence):
            return True 

    return False 

print(validateSubsequence(array, sequence))