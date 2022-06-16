def compressBits( A):
    len_A = len(A)
    ans = 0
    for i in range(len_A):
        for j in range(i, len_A):
            print("i - ",i," j -",j)
            if (i<j):
                A[i] = A[i] & A[j]
                A[j] = A[i] | A[j]
    print(A)
    for i in range(len_A):
        ans = ans ^ A[i]

    return ans





A=[1,3,5]
print(compressBits(A))