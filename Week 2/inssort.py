
import time

a = list(map(int, input().split()))

n = len(a)

st = time.process_time()

# write the insertion sort code into this segment
for i in range(1,len(a)) :
    key=a[i]
    j=i-1
    while j>=0 and a[j]>key:
    
        
        j-=1
    a.remove(key)
    a.insert(j+1,key)

        

    



    
et = time.process_time()

print(a)
print(et-st)
