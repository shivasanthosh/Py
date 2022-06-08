import math

A = [ 814, 761, 697, 483, 981 ]

def solve(A):
    arrSize = len(A)

    if arrSize == 1:
        return 1
    min_index = -1
    max_index = -1
    ans = arrSize
    # findmax
    maxN = -math.inf
    for i in range(arrSize):
        if A[i] > maxN:
            maxN = A[i]

    # findmin
    minN = math.inf
    for i in range(arrSize):
        if A[i] < minN:
            minN = A[i]

    if maxN == minN:
        return 1

    for i in range(arrSize - 1, -1, -1):
        if A[i] == maxN:
            max_index = i
            if min_index != -1:
                ans = min(ans, min_index - max_index + 1)
        if A[i] == minN:
            min_index = i
            if max_index != -1:
                ans = min(ans, max_index - min_index + 1)
    return ans

print(solve(A))










