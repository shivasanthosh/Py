class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(A):
        ans=[]
        for i in range(2**A):
            print(i>>1)
            print((i>>1)^i)
            ans.append((i>>1)^i)
            print()
        return ans

print(Solution.grayCode(3))