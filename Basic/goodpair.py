A = [1, 2, 3, 4]
B = 7


def solve(A, B):
    l = len(A)
    for i in range(l):
        for j in range(l):
            if A[i] + A[j] == B:
                return 1
    return 0


print(solve(A, B))
