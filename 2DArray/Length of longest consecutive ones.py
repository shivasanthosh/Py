A = "010100110101"
A = "1101001100101110"

A = "01"
A = "11100"

A = "010"

def solve(A):
    n = len(A)
    # LeftSum
    ls = [0 for _ in range(n)]
    ls[0] = int(A[0])
    l_count=0
    for i in range(n):
        if int(A[i])==1:
            l_count+=1
    if l_count==1:
        return 1
    for i in range(1,n):
        if (int(A[i]) == 0):
            ls[i] = 0
        else:
            ls[i] = int(A[i]) + ls[i - 1]

    print(ls)
    # RightSum
    rs = [0 for _ in range(n)]
    rs[n - 1] = int(A[n - 1])
    for i in range(n-2, -1, -1):
        if (int(A[i]) == 0):
            rs[i] = 0
        else:
            rs[i] = int(A[i]) + rs[i + 1]
    print(rs)
    massum=0
    for i in range(n):
        if int(A[i]) == 0:
            L = ls[i - 1] if i>0 else 0
            R = rs[i + 1] if i!=n-1 else 0
            sum = L + R + 1 if R!=0 else L
            massum = max(sum, massum)



    if l_count==massum:
        massum-=1

    return massum

print(solve(A))
