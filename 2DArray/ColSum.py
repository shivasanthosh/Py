A =[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 2, 3, 4]
]


def solve(A):
    col = len(A[0])
    row = len(A)
    result = [0 for _ in range(col)]

    for i in range(row):
        sum = 0
        for j in range(col):
            result[j]+=A[i][j]
    return result


print(solve(A))
