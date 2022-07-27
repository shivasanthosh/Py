def longestCommonPrefix(A):

    len_a = len(A)

    if len(A) == 0:
        return 0
    if len(A) == 1:
        return A[0]

    print(A)
    A.sort()
    print(A)

    last = min(len(A[0]), len(A[len_a - 1]))
    print(last)
    i = 0

    while (i < last and A[0][i] == A[len_a - 1][i]):
        print(i, " - ", A[0][i], " == ? ","------",len_a,"_", A[len_a-2][i])
        i += 1

    pre = A[0][0: i]
    return pre

A = ["abc", "abc", "abc","abd"]

print(longestCommonPrefix(A))

print(A[1][0:5])