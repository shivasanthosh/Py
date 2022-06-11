A = [
    [21, 62, 16, 44, 55, 100, 16, 86, 29],
    [62, 72, 85, 35, 14, 1, 89, 15, 73],
    [42, 44, 30, 56, 25, 52, 61, 23, 54],
    [5, 35, 12, 35, 55, 74, 50, 50, 80],
    [2, 65, 65, 82, 26, 36, 66, 60, 1],
    [18, 1, 16, 91, 42, 11, 72, 97, 35],
    [23, 57, 9, 28, 13, 44, 40, 47, 98]
]


def solve(A):
    row = len(A)
    col = len(A[0])

    rs = [[0 for _ in range(row)] for _ in range(col)]

    for i in range(len(rs)):
        for j in range(len(rs[0])):
            rs[i][j] = A[j][i]

    return rs
print(solve(A))
