class MergeSort:
    def merge(self, A, p, q, r):
        sub2 = q+1 #defining variable for starting index of second subarray
        #if A[q]<=A[sub2]:
        #    return;
        
        while(p<=q and sub2<r):
            if(A[p]<=A[sub2]):
                p+=1
            else:
                
                val = A[sub2]
                ind = sub2
                while(ind != p):
                    A[ind] = A[ind-1]
                    ind -= 1
                A[p] = val
                p+=1
                q+=1
                sub2+=1
            
            
    def sort(self, A, p, r):
        if p<r-1:
            mid = (p+r-1)//2
            self.sort(A,p,mid)
            self.sort( A,mid+1,r)
            self.merge(A,p,mid,r)