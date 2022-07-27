class Solution:
    def subsets(A):
        N = len(A)
        ans = []

        total_subset=1<<N
        for i in range(total_subset):
            curr_subset = []
            l=i
            for index in range(N):
                if l&1 == 1:
                    curr_subset.append(A[index])
                l=l>>1
            ans.append(curr_subset)

        return ans


A = [ 12, 13 ,14 ]

print(Solution.subsets(A))



