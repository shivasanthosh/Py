
def solve(A):
    len_a = len(A)
    ans=[]
    ans2=[]
    for i in range(len_a):
        ans=[]
        for j in range(i,len_a):
            if A[j] < 0:
                break
            ans.append(A[j])
        #print(ans)
        if (len(ans)>len(ans2)):
            ans2=ans
        #print(ans2)




    return ans2




A = [ 8986143, -5026827, 5591744, 4058312, 2210051, 5680315, -5251946, -607433, 1633303, 2186575 ]
#A=[1,2,3,4]
#5591744 4058312 2210051 5680315
print(solve(A))
