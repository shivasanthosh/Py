def solve(number):
    A = DeciToBinary(number)
    base=""
    for i in range(32):
        base+="0"
    base32Number=addBinary(base,A)
    x=reverse(base32Number)


    return binary_to_decimal(x)

def addBinary(a,b):
    res = ""
    carry, a, b = 0, a[::-1], b[::-1]
    for i in range(max(len(a), len(b))):
        digitA = int(a[i]) if i < len(a) else 0
        digitB = int(b[i]) if i < len(b) else 0
        total = digitA + digitB + carry
        res = str(total % 2) + res
        carry = total // 2
    if carry:
        res = "1" + res
    return res


def DeciToBinary(num):
    ans = ""
    n = int(num)
    while (n > 1):
        n = n // 2
        mod = n % 2
        ans += str(mod)
    if n==1:
        return str(1)
    return ans

def binary_to_decimal(number):
    k=len(number)
    sum=0
    for i in range(len(number),-1,-1):
        sum+=pow(2,i)
    return sum



def reverse(n):
    num=[]
    num[:0]=n
    s=""

    len_n=len(num)-1
    for i in range(len_n):
        num[len_n-i],num[i]=num[i],num[len_n-i]

    for i in range(len_n+1):
        s+=str(num[i])


    return s





numb = "8"
print(solve(numb))
