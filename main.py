def generateMatrix(n):
    # filling it with 0's
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    dirr = 0
    row, col = 0, 0
    num = 1
    k = 1

    while k <= n * n:
        matrix[row][col] = k
        k += 1
        if dirr == 0:
            col = col + 1
            if col == n or matrix[row][col] != 0:
                dirr = 1
                col -= 1
                row += 1
        elif dirr == 1:
            row = row + 1
            if row == n or matrix[row][col] != 0:
                dirr = 2
                col -= 1
                row -= 1
        elif dirr == 2:
            col = col - 1
            if col < 0 or matrix[row][col] != 0:
                dirr = 3
                col += 1
                row -= 1
        elif dirr == 3:
            row = row - 1
            if row < 0 or matrix[row][col] != 0:
                dirr = 0
                col += 1
                row += 1

    return matrix


def isPalindrome(A):
    string = A
    if string == string[:: -1]:
        return True
    return False




A = [[3, 0, 0, 0]
     [7, 4, 0, 0]
     [2, 4, 6, 0]
     [8, 5, 9, 3]
     ]

print(GetSumOfMax(A))
