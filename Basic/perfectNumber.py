import math
def main():
    num=input()
    for n in range(int(num)):
        print(isPerfect(input()))

    return 0

def isPerfect(num):
    sum=0
    num=int(num)
    max=math.floor(math.sqrt(num))
    print(max)
    for i in range(1,max+1):

        if num%i==0 :
            print(i)
            sum+=i
    if sum==num :
        return "YES"
    else :
        return "NO"

main()