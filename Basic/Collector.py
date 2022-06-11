A = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]

B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

A = [
  [4, 2],
  [1, 4]
]

B = [
  [5, 1],
  [5, 10]
]



def solve(A,B):

    dp=[[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    preSumB=[[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    suffSumA=[[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    l=len(A)
    m=len(A[0])
    #B Pre sum
    for i in range(l):
        for j in range(m):
            if j !=0:
                preSumB[i][j]=B[i][j]+preSumB[i][j-1]
            else:
                preSumB[i][j] = B[i][j]
    #A suff Sum
    for i in range(l):
        for j in range(m):
            if i!=0:
                suffSumA[i][j]=A[i][j]+suffSumA[i-1][j]
            else:
                suffSumA[i][j] = A[i][j]
    print(suffSumA)
    print(preSumB)
    if m==1:
        Ssum=0
        Psum=0
        for i in range(0,l):
            Psum+=preSumB[i][0]
        for j in range(0,l):
            Ssum+=suffSumA[j][0]
        if preSumB>suffSumA:
            return Psum
        else:
            return  Ssum
    if l==1:
        Ssum=0
        Psum=0
        for i in range(0,l):
            Psum+=preSumB[0][i]
        for j in range(0,l):
            Ssum+=suffSumA[0][j]
        if preSumB>suffSumA:
            return Psum
        else:
            return  Ssum
    #fill DP
    for i in range(l):
        for j in range(m):
            if i ==0 and j==0:
                if suffSumA[i][j]  >= preSumB[i][j]:
                    dp[i][j] = suffSumA[i][j]
                else:
                    dp[i][j] = preSumB[i][j]

            elif i == 0:
                if suffSumA[i][j]  >= preSumB[i][j] + dp[i][j - 1]:
                    dp[i][j] = suffSumA[i][j]
                else:
                    dp[i][j] = preSumB[i][j] + dp[i][j - 1]
            elif j==0:
                if suffSumA[i][j] + dp[i - 1][j] >= preSumB[i][j]:
                    dp[i][j] = suffSumA[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = preSumB[i][j]

            else:
                if suffSumA[i][j] + dp[i - 1][j] >= preSumB[i][j] + dp[i][j - 1]:
                    dp[i][j] = suffSumA[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = preSumB[i][j] + dp[i][j - 1]







    print(dp)
    return dp[l-1][m-1]

print(solve(A,B))

