A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
A = [
    [1, 2],
    [3, 4]
]

def solve(A):
    tm=transpose(A)
    r=rev(tm)
    return r

def rev(A):
    n = m = len(A)
    rs = [[0 for _ in range(n)] for _ in range(n)]
    k = 0
    i = 0

    while (i < m):
        mid = n // 2 + 1
        j = 0
        while (j < m):
            rs[i][j] = A[i][m - 1 - j]
            j += 1
        k += 1
        i += 1

    return rs


def transpose(Arr):
    row = len(Arr)
    col = len(Arr[0])
    rs = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(len(rs)):
        for j in range(len(rs[0])):
            rs[i][j] = Arr[j][i]

    return rs


print(solve(A))
