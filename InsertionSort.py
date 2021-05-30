class InsertionSort:
    def insertionsort(self, a):
        for i in range(1,len(a)):
            assert(len(a)>0)
            while(i>0 and a[i]<a[i-1]):
                assert(a[i-1]>a[i])
                a[i],a[i-1]=a[i-1],a[i]
                i=i-1
        return a 