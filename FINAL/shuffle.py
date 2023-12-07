from random import randrange

def shuffle(lt):
    for i in range(len(lt)-1,1,-1):

        j = randrange(i +1)
        lt[i],lt[j] = lt[j],lt[i] 

lt = [1, 2, 3, 4, 5, 6]
 
shuffle(lt)
 
# print the shuffled list
print(lt)
