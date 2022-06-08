B = 7
C = [ 3, 8, 8, 9, 7 ]

B = 78
C = [ 7, 1, 8, 5, 8, 5, 3, 3, 5 ]
import math

def solve(C, B):
    arr_size = len(C)
    ans = 0
    maxvalue = B
    for i in range(arr_size):
        sum = 0

        for j in range(i, arr_size):
            sum += C[j]
            print(sum,"<=",maxvalue)
            if sum <= maxvalue:
                if ans < sum:
                    ans = sum
                print("ans - ",ans)
    return ans

print(solve(C,B))