A = [
  [1, 2 ,3,4],
  [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]



def solve(A):
    n = m = len(A)

    rs = [[0 for _ in range(n)] for _ in range(n)]

    i = 0
    j = 0
    t=0
    currNumber = 1

    while m > 1:

        # o to n-1 left to right
        k = 0
        while (k < m - 1):
            p=k+t
            n = m - 1

            rs[i][j] = A[n-p][i]
            j += 1
            k += 1

        # o to n-1 left to right
        k=0
        while (k < m - 1):
            n = m - 1
            p = k + t
            rs[i][j] = A[n-p][k]
            i += 1
            k += 1

        # o to n-1 left to right
        k = 0
        while (k < m - 1):
            n = m - 1
            p = k + t
            rs[n][n - k] = A[p][n]
            j -= 1
            k += 1

        # o to n-1 left to right
        k = 0
        while (k < m - 1):
            n = m - 1
            p = k + t
            rs[i][j] = A[n][n-p]
            i -= 1
            k += 1



        i += 1
        j += 1
        m = m - 2
        t+=1

    if m%2!=0:
        mid= int(m/2)
        rs[mid][mid]=currNumber


    return rs


print(solve(A))
