
import functools

def myCompare(x, y):
    xy = x
    yx = y

    # Count length of x and y
    countx = 0
    county = 0

    # Count length of X
    while (x > 0):
        countx += 1
        x //= 10

    # Count length of Y
    while (y > 0):
        county += 1
        y //= 10

    x = xy
    y = yx

    while (countx):
        countx -= 1
        yx *= 10

    while (county):
        county -= 1
        xy *= 10

    # Append x to y
    yx += x

    # Append y to x
    xy += y
    print(xy," > ",yx)
    return False



def printLargest(arr):

    print(arr)
    arr.sort(key=functools.cmp_to_key(myCompare))
    print(arr)
    arr.reverse()
    print(arr)
    print("".join(map(str, arr)))

arr = [3, 30, 34, 5, 9]

printLargest(arr)