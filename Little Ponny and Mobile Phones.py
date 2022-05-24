A = [3, 4, 4, 6]
B = [20, 4, 10, 2]

def solve(A,B):
    result = [0 for _ in range(len(B))]

    sumList = presum(A)
    for i in range(len(B)):
        result[i] = returnCount(sumList, 10)
    return result





def returnCount(sumList,Bi):
    x = findIndex(sumList, Bi)
    if x == -1:
        return findlastIndex(sumList,Bi)+1
    else:
        return x+1

def findlastIndex(arr,find):
    first = 0
    last = len(arr)
    findlastValue=0
    while first < last:

        mid = (first + last) // 2

        if arr[mid] == find:
            return mid
        elif arr[mid] < find:
            if findlastValue < arr[mid]:
                findlastValue = arr[mid]
            first = mid + 1
        else:
            if findlastValue<arr[mid]:
                findlastValue=arr[mid]
            last = mid - 1


    return findIndex(arr,findlastValue)

def findIndex(arr,find):
    first=0
    last=len(arr)
    while first<last:

        mid = (first+last)//2

        if arr[mid]==find:
            return mid
        elif arr[mid]<find:
            first=mid+1
        else:
            last=mid-1

    return -1



def presum(A):
    length = len(A)
    preSum = [0 for _ in range(length)]
    preSum[0]=A[0]
    for i in range (1,length):
        preSum[i]=preSum[i-1]+A[i]
    return preSum



print(solve(A,B))