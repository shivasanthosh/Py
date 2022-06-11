
A = [
  [15, 1, 10],
  [5, 19, 19],
  [3, 5, 6],
  [6, 2, 8],
  [2, 12, 16],
  [3, 8, 17],
  [12, 5, 3],
  [14, 13, 3],
  [2, 17, 19],
  [16, 8, 7],
  [12, 19, 10],
  [13, 8, 20]
]

B = [[1, 2, 2, 3, 5],
  [3, 2, 3, 4, 4],
  [2, 4, 5, 3, 1],
  [6, 7, 1, 4, 5],
  [5, 1, 1, 2, 4]]

def BlueLake(A):
    BlueLake = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

    col = 0
    row = 0
    m = len(A)
    n= len(A[0])
    k = 1
    for row in range(len(A)):
        for col in range(n):
            if row != 0 and col != 0:
                if A[row][col] >= A[row][col-1] or \
                        A[row][col] >= A[row - 1][col]:
                    if BlueLake[row][col-1] != 0:
                        BlueLake[row][col] = A[row][col]
                    else:
                        BlueLake[row][col] = 0
                else:
                    BlueLake[row][col] = 0
            else:
                BlueLake[row][col] = A[row][col]
    return BlueLake






def Redlake(A):
    Redlake = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

    col = 0
    row = 0
    maxIndex = len(A)-1
    colMax = len(A[0])-1
    for row in range(maxIndex, -1, -1):
        for col in range(colMax, -1, -1):
            if row != maxIndex and col != colMax:
                if A[row][col] >= A[row][col+1] or \
                        A[row][col] >= A[row + 1][col]:
                    if Redlake[row][col + 1] != 0:
                        Redlake[row][col] = A[row][col]
                    else:
                        Redlake[row][col] = 0

                else:
                    Redlake[row][col] = 0
            else:
                Redlake[row][col] = A[row][col]
    return Redlake

def do(A,B):
    count = 0
    row = 0
    col = 0
    m = len(A)
    n = len(A[0])
    for row in range(m):
        for col in range(n):
            print("row ", row , "col ", col, " - ", A[row][col]," ?",B[row][col])
            if A[row][col] == B[row][col] :
                if A[row][col] != 0:
                    count += 1
                print("c " , count)
    return count

Red = Redlake(A)
print(A)
print(Red)
Blue = BlueLake(A)
print(Blue)

print(do(Red,Blue))


