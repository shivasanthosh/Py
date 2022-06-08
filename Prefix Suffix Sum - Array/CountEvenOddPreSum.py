A = [4,2,-2]

def solve(A):
    ans=len(A)
    orgArr=A.copy()
    for i in range(len(A)):

        if removeandCheck(orgArr)==1:
            ans-=1
    return ans

def removeandCheck(A):
    preEvenSum=preEven(A)
    preOddSum = preOdd(A)
    size=len(A)-1
    if preOddSum[size]==preEvenSum[size]:
        return 1
    else:
        return 0




def preEven(A):
    size=len(A)
    arr=[0 for _ in range(size)]
    arr[0]=A[0]
    for i in range(1,size):
        if i%2==0:
            arr[i]=A[i]+arr[i-1]
        else:
            arr[i]=arr[i-1]
    return arr

def preOdd(A):
    size=len(A)
    arr=[0 for _ in range(size)]
    arr[0]=0
    for i in range(1,size):
        if i%2!=0:
            arr[i]=A[i]+arr[i-1]
        else:
            arr[i]=arr[i-1]
    return arr







print(solve(A))