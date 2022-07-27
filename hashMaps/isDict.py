class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):

        len_a = len(A)
        alpha_dic = {}

        second_dic = {}

        if len_a == 1:
            return 1

        for i in range(len(B)):
            if B[i] not in alpha_dic:
                alpha_dic[B[i]] = i

        for i in range(len(A) - 1):
            status = self.compareStrings(A[i], A[i + 1], alpha_dic)
            print(status)
            if not status:
                return 0
        return 1

    def compareStrings(self, string1, string2, alpha_dic):
        i = 0
        while (i < len(string1) and i < len(string2)):
            val1 = alpha_dic.get(string1[i])
            val2 = alpha_dic.get(string2[i])
            i += 1
            if (val1 < val2):
                return True
            elif (val1 > val2):
                return False
        if i < len(string1):
            return False
        return True








