A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

def solve(A):
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    for i in range(n // 2):
        for j in range(n):
            A[j][n - i - 1], A[j][i] = A[j][i], A[j][n - i - 1]
    return A

print(solve(A))
