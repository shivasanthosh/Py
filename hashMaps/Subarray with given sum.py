A = [5, 10, 20, 100, 105]
B = 105


def solve(A, B):
    n = len(A)
    l, r = 0, 0
    sub_sum = 0
    while (l < n and r < n):
        if sub_sum < B:
            sub_sum += A[r]
            r += 1

        if sub_sum > B:
            sub_sum -= A[l]
            l += 1

        print(" l - ",l," r - ",r-1," sum - ",sub_sum)
        if sub_sum == B:
            return A[l:r]

    return [-1]

print(solve(A,B))