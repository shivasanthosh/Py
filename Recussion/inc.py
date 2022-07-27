def bar(x, y) :
    if y == 0:
        return 0
    return (x + bar(x, y-1))
def foo(x, y) :
    if(y == 0):
        return 1
    return bar(x, foo(x, y-1) )
#print(foo(3, 5))


def fun(x, n) :
    if(n == 0) :
        return 1
    elif (n % 2 == 0):
        return fun(x *  x,n//2)
    else:

        return x * fun(x * x, (n - 1) // 2)
ans=fun(2, 10)
print(ans)