A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# [1 0 0 ] [2 4 0 ] [3 5 7 ] [6 8 0 ] [9 0 0 ]

def solve(A):
    col = len(A[0])
    row = len(A)
    rs = []
    # AntiDig
    r = 0
    c = 0
    ls = []
    while (r < row):
        i = r
        j = c
        # print diagonal
        ls=[]
        while (i < row and col > j > -1):
            print("----")
            print(A[i][j])
            ls.append(A[i][j])
            print("i - ", i, " j - ", j)

            i += 1
            j -= 1


        if (c < col):
            c += 1
        else:
            r += 1
            c -= 1
        if(len(ls)!=0):
            ln=len(ls)
            while(ln<col):
                ls.append(0)
                ln+=1
            rs.append(ls)


    return rs


print(solve(A))
