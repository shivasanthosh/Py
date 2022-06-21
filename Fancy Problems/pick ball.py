blue_count=20
red_count=14
ls=[]

for i in range(14):
    ls.append("Red")

for i in range(20):
    ls.append("Blue")



import random


def solve(ls):
    n=len(ls)
    while(n>0):
        if (random.choice(ls)=='Blue' and random.choice(ls)=="Blue"):
            ls.pop(ls.index("Blue"))
            ls.pop(ls.index("Blue"))
            ls.append("Blue")
        elif (random.choice(ls)=="Red" and random.choice(ls)=="Blue"):
            ls.pop(ls.index("Red"))
            ls.pop(ls.index("Blue"))
            ls.append("Red")
        elif (random.choice(ls)=="Red" and random.choice(ls)=="Red"):
            ls.pop(ls.index("Red"))
            ls.pop(ls.index("Red"))
            ls.append("Blue")

        n = len(ls)
        print(n,"-",ls)


print(solve(ls))

