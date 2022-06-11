#Availve service
A = 1
#microsecond delay
B = 3
#orders
C = [1, 4, 5, 9, 10, 14, 15, 18, 19, 20]

# 5 6 11 16
# 3 2 3 3
def isNegative(D):
    if D < 0:
        return 0
    return D
def solve(A,B,C):
    l = len(C)
    container = []
    avaiable = [0 for _ in range(l)]

    for i in range(l):
        container.append(C[i]+B)
        for j in range(len(container)-1, -1, -1):
            if container[j] <= C[i]:
                avaiable[i] = A - len(container)
                container.pop(0)
        avaiable[i] = isNegative(A - len(container))




    return avaiable

print(solve(A,B,C))




