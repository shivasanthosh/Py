class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(A, B):

        def oneComplement(A):
            s = ''
            for i in range(len(A)):
                if A[i] == '0':
                    s += '1'
                else:
                    s += '0'
            return s

        def row(A):
            if A == 1:
                return '0'
            s = row(A - 1)

            return s + oneComplement(s)

        r = row(A)

        return r[B - 1]


print(Solution.solve(4,1))