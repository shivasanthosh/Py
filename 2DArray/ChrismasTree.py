import math

A =[1 ,2 ,3, 4, 5 ,6, 7 ,8, 9 ,10]
B =[10, 13 ,11, 14, 15, 12 ,13, 13, 18 ,13]
def solve(A, B):
    l = len(A)
    min = math.inf
    for i in range(l):
        for j in range(i + 1, l):
            for k in range(j + 1, l):
                sum=0
                print(i, " ", j, " ", k)
                if (A[i] < A[j] < A[k]):

                    sum += B[i] + B[j] + B[k]
                    print("----", A[i], "+", A[j], "+", A[k],"=",sum)
                    if sum < min:
                        min = sum
                        print("#min ", min)



    if min == math.inf:
        return -1
    return min

print(solve(A,B))