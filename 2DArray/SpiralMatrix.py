A = 80


def solve(A):
    n = m = A

    rs = [[0 for _ in range(n)] for _ in range(n)]

    i = 0
    j = 0
    currNumber = 1

    while n > 1:

        # o to n-1 left to right
        k = 1
        while (k <= n - 1):
            rs[i][j] = currNumber
            currNumber += 1
            j += 1
            k += 1

        # o to n-1 top to bottom
        k = 1
        while (k <= n - 1):
            rs[i][j] = currNumber
            currNumber += 1
            i += 1
            k += 1

        # n-1 to n-1 top to bottom
        k = 1
        while (k <= n - 1):
            rs[i][j] = currNumber
            currNumber += 1
            j -= 1
            k += 1

        # n-1 to n-1 top to bottom
        k = 1
        while (k <= n - 1):
            rs[i][j] = currNumber
            currNumber += 1
            i -= 1
            k += 1

        i += 1
        j += 1
        n = n - 2

    if m%2!=0:
        mid= int(m/2)
        rs[mid][mid]=currNumber


    return rs


print(solve(A))
