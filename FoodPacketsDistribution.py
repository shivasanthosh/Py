import math
A = [2, 9, 5, 4 ]
B = 13

def SumOfList(A):
    sum = 0
    for i in range(len(A)):
        sum += A[i]
    return sum

def check(k):
    req = 0
    for i in range(len(A)):
        req += (A[i]/k)
    if req >= B :
        return True



def solve(A,B):
    if SumOfList(A) < B:
        return 0
    l = 1
    r = min(A)
    result = 0
    while l <= r :
        mid = int((l+r)/2)
        if check(mid):
            result = mid
            l = mid + 1
        else:
            r = mid - 1
    return result

print(solve(A, B))







