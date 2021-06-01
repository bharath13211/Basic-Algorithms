class BinarySearch:
    
    def search(self,A,key):
        start = 0
        end = len(A)-1
        while(end>=start):
            mid = start+((end-start)//2)
            if A[mid]==key:
                return mid
            if A[mid]>key:
                end = mid-1
            if A[mid]<key:
                start = mid+1
        return -1
