class QuickSelect:
    def partition(self, A: [int], lo: int, hi: int) -> int:
        sublist = []
        median = []
        for i in range(lo,hi):
            sub = A[i:i+5]
            for i in range(0,len(sub)):
                for j in range(i,len(sub)):
                    if sub[i] > sub[j]:
                        sub[i],sub[j] = sub[j],sub[i]
            sublist.append(sub)
            median.append(sub[(len(sub)//2)-1])
    #median.sort()
        for i in range(0,len(median)):
            for j in range(i,len(median)):
                if median[i] > median[j]:
                    median[i],median[j] = median[j],median[i]
        return median[len(median)//2]
        #if len(median) <= 5:
            #return median[len(median)//2]
        #else:
            #partition(median,0,len(median))
        
    def partition1(self, A: [int], lo: int, hi: int) -> int:
        sublists = [A[j:j+5] for j in range(lo, hi, 5)]
        for sub in sublists:
            sub.sort()
        med = [sublist[len(sublist)//2] for sublist in sublists]
        med.sort()
        #print("partition function",sublists, med)
        if len(med) <= 5:
            return med[len(med)//2]
        else:
            return self.partition1(med,0,len(med))
    def select(self, A: [int], k: int) -> int:
        while(len(A)>0):
        
            pivot = self.partition1(A,0,len(A))
            #print(pivot)
            low = []
     
            high = []
            for i in A:
                if pivot > i:
                    low.append(i)
                if pivot < i:
                    high.append(i)
            #print(low,high)
            piv_ind = len(low)
            if piv_ind == k:
                return pivot
            elif piv_ind > k:
                return self.select(low,k)
            elif piv_ind < k:
                return self.select(high,(k-piv_ind-1))