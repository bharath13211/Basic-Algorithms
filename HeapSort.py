class HeapSort:
    def heapify(self, A, n, i):
        largest = i  
        l = 2 * i + 1
        r = 2 * i + 2 
        if l < n and A[largest] < A[l]:
            largest = l
        if r < n and A[largest] < A[r]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.heapify(A, n, largest)
            
    def heapSort(self, A):
        n = len(A)
        for i in range(n//2 - 1, -1, -1):
            self.heapify(A, n, i)
        for i in range(n-1, 0, -1):
            A[i], A[0] = A[0], A[i]
            self.heapify(A, i, 0)