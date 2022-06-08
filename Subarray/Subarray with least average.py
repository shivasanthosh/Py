A = [15, 7, 11, 7, 9, 8, 18, 1, 16, 18, 6, 1, 1, 4, 18]
B = 6

import math


def solve(A, B):
    ps = preSum(A)
    arr_size = len(A)
    minaverage = math.inf
    index = -1
    avgsum = 0
    k = B
    i = 0
    while (k <= arr_size):

        j = i + B - 1
        print("i - ",i," j - ",j)
        if i == 0:
            avgsum = ps[B-1]
        else:
            avgsum = ps[j] - ps[i - 1]
        print(avgsum," < ",ps[j] - ps[i - 1])
        if avgsum < minaverage:
            minaverage = avgsum
            index = i
            print("index - ",index)

        i += 1
        k += 1
    return index

    # for i in range(arr_size):
    #     sum = 0
    #     for j in range(i + B - 1, arr_size - B):
    #         print("------------")
    #         print("i - ",i," j - ",j)
    #         sum = sum + A[j]
    #         print(int(sum / B),"<",minaverage)
    #     if int((sum / B)) < minaverage:
    #         minaverage = int((sum / B))
    #         index = i
    #         print("Index - ",index)
    # return index


def preSum(A):
    arr_size = len(A)
    preSum = [0 for _ in range(arr_size)]
    preSum[0] = A[0]
    for i in range(arr_size):
        preSum[i] = A[i] + preSum[i - 1]
    return preSum


print(solve(A, B))
