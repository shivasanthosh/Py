A = "100"
B = "11"


def solve(a, b):
    res = ""
    carry, a, b = 0, a[::-1], b[::-1]
    for i in range(max(len(A), len(B))):
        digitA = int(A[i]) if i < len(a) else 0
        digitB = int(B[i]) if i < len(b) else 0
        total = digitA + digitB + carry
        res = str(total % 2) + res
        carry = total // 2
    if carry:
        res = "1" + res
    return res

def carry():
    c=0
    if c:
        print(c)

print(carry())
