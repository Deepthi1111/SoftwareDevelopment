"""
Give me the largest possible value for the expression:
array[a] - array[b] + array[c] - array[d] where the indices, a < b < c < d
"""

"""
We want to maximize the value of array[a] and array[c] and minimize the value of array[b] and array[d] to maximize the value of overall expression.
Say A = array[a]
AminusB = array[a] - array[b]
AminusBplusC = array[a] - array[b] + array[c]
AminusBplusCminusD = array[a] - array[b] + array[c] - array[d]
"""

array = [3, 6, 1, -3, 2, 7, 5, 3, 7, 2, 8, 4, 8, 4, 7, 2, 9]

def evaluateMaximumValueOfThisFixedExpression(array):
    A = [None] * len(array)
    AminusB = [None] * len(array)
    AminusBplusC = [None] * len(array)
    AminusBplusCminusD = [None] * len(array)

    A[0] = array[0]
    for i in range(1, len(array)):
        A[i] = max(array[i], A[i - 1])

    AminusB[1] = A[0] - array[1]
    for i in range(2, len(array)):
        AminusB[i] = max(AminusB[i - 1], A[i - 1] - array[i])

    AminusBplusC[2] = AminusB[1] + array[2]
    for i in range(3, len(array)):
        AminusBplusC[i] = max(AminusBplusC[i - 1], AminusB[i - 1] + array[i])

    AminusBplusCminusD[3] = AminusBplusC[2] - array[3]
    for i in range(4, len(array)):
        AminusBplusCminusD[i] = max(AminusBplusCminusD[i-1], AminusBplusC[i-1] - array[i])

    return AminusBplusCminusD[-1]

print(evaluateMaximumValueOfThisFixedExpression(array))

    




