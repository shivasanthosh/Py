def solve():
    A = [1, 2, 3, 4, 5]
    B = 5
    N = len(A)
    ps = [0 for _ in range(N)]

    ps[0] = A[0]
    for i in range(1, N):
        ps[i] = A[i] + ps[i - 1]
    print(ps)
    l = 0
    r = N - 1
    while (l < r):

        if l != 0:
            x = ps[r] - ps[l - 1]
        else:
            x = ps[r]
        print(x)
        print("i -",l," j - ",r)
        if x == B:
            return A[r:l]
        elif x >= B:
            r -= 1
        else:
            l += 1
    return -1

print(solve())




