array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

"""
Kadane's Algorithm: Gets the maximum sum that can be obtained by taking any sub-array from the given array.
In this case the subarray which yeilds max sum is array[3:15]
"""

def kadanesAlgorithm(array):
    maxSumOverall = float("-inf")
    maxSumThusFar = [float("-inf")] * len(array)
    maxSumThusFar[0] = array[0]
    startIdx = None
    endIdx = None
    for i in range(1, len(array)):
        if array[i] + maxSumThusFar[i-1] > array[i]:
            maxSumThusFar[i] = array[i] + maxSumThusFar[i-1]
        else:
            maxSumThusFar[i] = array[i]
            startIdx = i

        if maxSumThusFar[i] > maxSumOverall:
            maxSumOverall = maxSumThusFar[i]
            endIdx = i 

    return maxSumOverall
        
print(kadanesAlgorithm(array))







