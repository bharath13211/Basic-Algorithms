class MajorityElement:
    def majority(self, A):
        d={}
        #if len(A)%2 == 0:
        l = len(A)//2
        #elif len(A)%2 == 1:
        #    l = (len(A)//2)+1 
        for i in A:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
    #print(d)
        for i in d.keys():
        #print(d[i])
            if d[i] > l:
                return i
        return -1