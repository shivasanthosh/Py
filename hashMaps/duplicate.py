class FindDuplicate:
    def solve(Arr):
        hashset= set()

        for n in Arr:
            if n in hashset:
                print(n)
                return True
            hashset.add(n)
        return False


A=[1,2,3,4,5,4,6,7]

print(FindDuplicate.solve(A))
