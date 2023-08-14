# R=[int(i) for i in input().split(",")]
# R.sort()
# value=int(input())
# k=int(input())


import time

def insertion(R,k,value):
    i=len(R)-1
    while i>=0 and R[i]>value:
        
        i-=1
    # if i>=0 and (((i==len(R) -1) or abs(R[i]-value>=k)) and ((i==0) or abs(R[i-1]-value)>=k)):
    if i >= 0 and (((i == len(R) - 1) or abs(R[i] - value) >= k) and ((i == 0) or abs(R[i - 1] - value) >= k)):
        R.insert(i+1,value)
        return True
    else :
        return False
R = [17,21,26,29,36]
value = [8,19,24,33,40]
k=3

st=time.process_time()
for i in value:
    if insertion(R,k,i)==True:
        print(R)
        print("reservation success")
    else:
        print("reservation failed")
        print(R)                           
et=time.process_time()
print(st-et)

#the time ocmplxity of above algorithm is O(n)
