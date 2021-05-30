class InversionCount:
    def count(self, A: [int]) -> [int]:
        C=[0]*(len(A))
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if A[i]>A[j]:
                    C[i] += 1
        return C