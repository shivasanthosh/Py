import math


def numberOfDigit(n):
    count = 0
    while (n > 0):
        count += 1
        n = n // 10
    return count


def isAmstrong(n):
    l = numberOfDigit(n)
    temp = n
    sum = 0
    while temp > 0:
        lastDigit = temp % 10
        sum = sum + math.pow(lastDigit, l)
        temp = temp // 10
    if sum == n and 1<n<10:
        return True
    return False


print(isAmstrong(2))
