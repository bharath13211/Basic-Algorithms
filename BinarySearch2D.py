class BinarySearch2D:
    def search(self, M: [[int]], q: int) -> [int, int]:
        if len(M) == 0:
            return [-1,-1]
        if len(M[0]) == 0:
            return [-1,-1]
        i = 0
        j = len(M[0])-1
        while(i<=(len(M)-1) and j>=0 ):
            if M[i][j] == q:
                return [i,j]
            if M[i][j]>q:
                j-=1
            if M[i][j]<q:
                i+=1
        return [-1,-1]