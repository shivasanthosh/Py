A = [3, 4, 4, 6]
B = [20, 4, 10, 2]

#pre sum
def presum(A):
    result = [0 for _ in range(len(A))]
    result[0] = A[0]

    for i in range(1,len(A),1):
        result[i] = result[i-1]+A[i]

    return result
#hello
#test
def binarySearch(arr,find):
    min = 0
    max = len(arr) - 1
    while min <= max:
        mid = min + (max - min) // 2



        if (arr[mid] == find):
            return mid
        elif arr[mid] < find:
            min = mid + 1
        else:
            max = mid - 1
    return -1


def SecondlargestIndex(arr, find):
    min = 0
    max = len(arr) - 1
    while min <= max:
        mid = min + (max - min) // 2

        if (arr[mid-1] < find):
            return mid-1
        elif arr[mid] < find:
            min = mid + 1
        else:
            max = mid - 1
    return -1

print(presum(A))

x = binarySearch(presum(A),18)
if x != -1 :
    print(x)
else:
    print(SecondlargestIndex(presum(A),18))



