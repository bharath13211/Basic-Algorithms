import random
class QuickSort:
	def partition(self, A, p, r):
		piv_ind = random.randrange(p, r)
		i = p-1
		#j=p
		A[r-1],A[piv_ind] = A[piv_ind],A[r-1]
		pivot = A[r-1]
		for j in range(p,r-1):
			if A[j]<=pivot:
				i+=1
				A[i],A[j] = A[j],A[i]
		A[i+1], A[r-1] = A[r-1],A[i+1]
		return (i+1)
				
				
		
		
	
	def sort(self, A, p, r):
		if p<r:
			prev_pivot = self.partition(A,p,r)
			
			self.sort(A,p,prev_pivot)
			self.sort(A,(prev_pivot+1),r)