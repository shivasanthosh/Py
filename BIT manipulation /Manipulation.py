def solve(number):
    res = 0
    for _ in range(32):
        res = res << 1
        print("<<",res)
        res =res+ (number % 2)
        number = number >> 1
        print(number,"--------",res)

    return res


print(solve(5))
