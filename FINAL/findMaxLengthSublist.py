#myself
import random

randomList = []
for i in range(5):
    n = random.randint(1,30)
    randomList.append(n)

print(randomList)

max = 0
max_i = max_j = -1
for i in range(len(randomList)):
    for j in range(i+1, len(randomList)):
        if randomList[i] * randomList[j] > max:
            max =  randomList[i] * randomList[j]
            (max_i, max_j) = (randomList[i] , randomList[j])

print(f"pair is ({max_i}, {max_j})")

print("---------------------------------")
import sys
 
# A naive solution to finding the maximum product of two integers in a list
def findMaximumProduct(A):
 
    # base case
    if len(A) < 2:
        return
 
    max_product = -sys.maxsize
    max_i = max_j = -1
 
    # consider every pair of elements
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            # update the maximum product if required
            if max_product < A[i] * A[j]:
                max_product = A[i] * A[j]
                (max_i, max_j) = (i, j)
 
    print("Pair is", (A[max_i], A[max_j]))
 
 
if __name__ == '__main__':
 
    A = [-10, -9, -7, -7, -4, -3, 0, 4, 5, 6, 6, 8, 8, 8, 10]
    findMaximumProduct(A)