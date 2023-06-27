
def merge(A, p, q, r):
    B = []
    i = p
    j = q+1
   
    while i <= q and j <= r:
        
        if A[i] <= A[j]:
            
            
            B.append(A[i])
            
            i += 1
        else:
            
            B.append(A[j])
            
            j += 1


    
    
    A[p:r+1] = B + A[i:q+1] + A[j:r+1]
    

#def mergesort(A, p, r):
def mergesort(A,p,r):
     if p < r:
        q = (p + r) // 2



        
        mergesort(A, p, q)     # Recursively sort the first half of the array

         
        mergesort(A, q+1, r)   # Recursively sort the second half of the array
          
          
        merge(A, p, q, r)      # Merge the two sorted halves

   


a = list(map(int, input().split()))
print(a)

import time

st = time.process_time()

mergesort(a, 0, len(a)-1)

et = time.process_time()

print(a)
print(et-st)
