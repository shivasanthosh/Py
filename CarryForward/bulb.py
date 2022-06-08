A = [ 1, 1, 0, 0, 1, 1, 0, 0,1]


def bulbs( A):
    arrSize = len(A)


    count=0
    for i in range(1, arrSize):
        if A[i] != A[i - 1]:
            count += 1
            print(count)
    return count

print(bulbs(A))
