A = [3, 4, 4, 6]
B = [20, 4, 10, 2]

A = [ 25, 43, 47, 95, 98 ]
B = [ 184, 533, 811, 330, 509, 192 ]

A = [ 23, 36, 58, 59 ]
B = [ 3, 207, 62, 654, 939, 680, 760 ]


def solve( A, B):
    result = [0 for _ in range(len(B))]
    Asum = [0 for _ in range(len(A))]
    Asum[0] = A[0]
    for n in range(0, len(A)):
        print(A[n])
        Asum[n] = Asum[n-1] + A[n]
    print(Asum)
    for i in range(len(B)):
        value = findIndex(Asum, B[i])
        if value == -1:
            result[i] = secondlargest(Asum, B[i]) + 1
        else:
            result[i] = value + 1
    print(result)
    return result

def findIndex( arr, find):
    left = 0
    right = 0
    while (left < right):
        mid = left + right // 2
        if arr[mid] == find:
            return mid
        elif arr[mid] > find:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def secondlargest(arr, find):
    max = len(arr)
    for i in range(max-1, -1, -1):
        if arr[i] < find:
            return i
    return -1

solve(A,B)


