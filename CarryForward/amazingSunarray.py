A = "pGpEusuCSWEaPOJmamlFAnIBgAJGtcJaMPFTLfUfkQKXeymydQsdWCTyEFjFgbSmknAmKYFHopWceEyCSumTyAFwhrLqQXbWnXSn"


def solve(A):
    arrSize = len(A)
    ans = 0

    for i in range(arrSize):

        if check(A[i]):
            print(A[i])
            ans = ans + arrSize - i
            print(i," ",ans)
    return ans % 10003

def check(Value):
    arr=["a","e","i","o","u","A","E","I","O","U"]

    for i in range(len(arr)):
        if Value==arr[i]:
            return True
    return False

print(solve(A))

