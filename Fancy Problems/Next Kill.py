import math
def solve(N):

    return 2*(N-math.pow(2,int(math.log2(N))))+1

print(solve(100))


