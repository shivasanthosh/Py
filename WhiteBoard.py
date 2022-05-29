def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    arr = []
    arr = [int(item) for item in input().split()]
    arr = arr[1:]
    k = int(input())
    l = len(arr)
    k = k % l
    arr = rev(arr, 0, l - k - 1)
    arr = rev(arr, l - k, l - 1)
    arr = rev(arr, 0, l - 1)
    for _ in arr:
        print(_, end=" ")
    return 0


def rev(arr, startIndex, endIndex):
    while startIndex < endIndex:
        temp = arr[startIndex]
        arr[startIndex] = arr[endIndex]
        arr[endIndex] = temp
        startIndex += 1
        endIndex -= 1
    return arr


if __name__ == '__main__':
    main()
