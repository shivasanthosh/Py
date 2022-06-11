def solve( A, B):
   #print(rotate(A,2))
    print(rotate(A,2))


    print(rotate(A, 1))


    return 0


def rotate( rA, rotateCount):
    arr_size = len(rA)

    rotateCount = rotateCount % arr_size
    rA = rev(rA, 0, rotateCount - 1)
    rA = rev(rA, rotateCount, arr_size - 1)
    rA = rev(rA, 0, arr_size - 1)
    return rA


def rev( arr, startIndex, endIndex):
    while (startIndex < endIndex):
        temp = arr[startIndex]
        arr[startIndex] = arr[endIndex]
        arr[endIndex] = temp
        startIndex += 1
        endIndex -= 1
    return arr

A = [ 1, 2, 3, 4, 5 ]
B = [ 2, 3 ]

print(solve(A,B))
