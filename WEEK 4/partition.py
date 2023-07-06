import sys
import time
#quick sort is very fast, so  we do not use time, instead we use counter



def partition(A, l, r):  # Lomuto's partition scheme
    global COUNTER
    x = A[r]
    i = l-1
    for j in range(l, r):
        COUNTER += 1
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[r],A[i+1] = A[i+1],A[r]
    return i+1


def quickSort(A,l,r):
    if l<r:
        p=partition(A,l,r)
        quickSort(A,l,p-1)
        quickSort(A,p+1,r)
# #def partition(A,left,right):
#     i =left
#     j=right-1
#     pivot= A[right]
#     while i<j:
#         while i<right and A[i]<pivot:
#             i+=1
#         while j>left  and A[j]>=pivot:
#             j-=1
#         if i<j:
#             A[i],A[j]=A[j],A[i]

#     if A[i]>pivot:
#         A[i],A[right]=A[right],A[i]
#     return i;

COUNTER=0
sys.setrecursionlimit(1000000)

st = time.process_time()
A= list(map(int, input().split(",")))
print(A)
quickSort(A,0,len(A)-1)
print(A)
et = time.process_time()
print(et-st)
print(COUNTER)





# A = [5, 2, 8, 1, 6, 3]
# print(A)
# quickSort(A,0,len(A)-1)
# print(A)







# A = [1, 3, 2, 4, 5]
# p = 0
# r = len(A) - 1

# result = partition(A, p, r)

# print("Test case 1:")
# print("Input:", A)
# print("result:", result)

# print("")

# A = [3,2,1,-1,-2,-3,0]
# p = 0
# r = len(A) - 1

# result = partition(A, p, r)

# print("Test case 2:")
# print("Input:", A)
# print(A[:result],A[result+1:])
# print("result:", result)

# print("")