import  math

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(A):
        M=(10**9)+7
        ans=0
        N=len(A)
        #max element from the list
        maxelement=max(A)
        #this will give us max bit
        iteration = int(math.log(maxelement,2))+1

        for i in range(iteration):
            setbittracker=0
            for j in range(N):
                if (A[j]>>i)&1:
                    setbittracker=j+1
                ans+=setbittracker*(2**i)
        return ans%M

arr=[1, 2, 3, 4, 5]
print(Solution.solve(arr))
