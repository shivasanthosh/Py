import math

A =[1 ,2 ,3, 4, 5 ,6, 7 ,8, 9 ,10]
B =[10, 13 ,11, 14, 15, 12 ,13, 13, 18 ,13]


def solve(A, B):
    flag = 0
    ans = 0
    l = len(A)
    for i in range(1, l - 1):
        minn = 0
        f = 0
        anss = B[i]

        for j in range(i - 1, -1, -1):
            if (A[j] < A[i]):
                if f == 0:
                    f = 1
                    minn = B[j]
                    # print(minn)
                else:
                    minn = min(minn, B[j])
                    # print(minn)

        if (f == 0):
            continue
        anss += minn
        # print(ans)
        minn = 0
        f = 0

        for j in range(i + 1, l):
            if (A[j] > A[i]):
                if f == 0:
                    f = 1
                    minn = B[j]
                else:
                    minn = min(minn, B[j])

        if (f == 0):
            continue

        anss += minn
        # print(ans)
        if flag == 0:
            ans = anss

        else:
            ans = min(ans, anss)
        flag = 1
    if flag == 1:
        return ans
    else:
        return -1

print(solve(A,B))