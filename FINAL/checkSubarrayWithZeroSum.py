import random
import re
def hasZeroSumSublist(lt):
    s = set()
    s.add(0)
    
    total = 0

    for i in lt:
        total += i

        if total in s:
            return True
        
        s.add(total)
        print(s)

    return False    

randomList = []
for i in range(10):
    n = random.randint(-10,10)
    randomList.append(n)

print(randomList)

if hasZeroSumSublist(randomList):
    print("SUblist exist")
else:
    print("SUblist does not exist")