# import sys

# n = int(sys.argv[1])

# # quicksort worst-case gen

# import random

# k = 0
# while k < n:
#     i = random.randint(0, 4*n)-2*n
#     p = random.randint(0,10000)/10000
#     if p <= 0.25:
#         print(i, end=' ')
#         k += 1



# quicksort worst-case gen

import random
import csv
import sys
def dataGenerator (dataSize, outputfile):
    with open(outputfile,'w' ,newline= '') as csvfile:
        wr =csv.writer(csvfile,delimiter=",")
        data=[]
        for x in range (0,dataSize):
            data.append(random.randint(0,dataSize))
        wr.writerow(data)
if __name__=="__main__":
    try:
        dataGenerator(int(sys.argv[1]),sys.argv[2])
    except(IndexError,ValueError):
        print("Usage: %s <dataSize> [outputfile]" %sys.argv[0])


# def dataGenerator(dataSize, outputfile):
#     with open(outputfile, 'w') as file:
#         data = random.sample(range(dataSize), dataSize)
#         for item in data:
#             file.write(str(item) + '\n')

# if __name__ == "__main__":
#     if len(sys.argv) < 3:
#         print("Usage: %s <dataSize> <outputfile>" % sys.argv[0])
#     else:
#         try:
#             dataGenerator(int(sys.argv[1]), sys.argv[2])
#             print("Data generation successful!")
#         except (ValueError, OSError) as e:
#             print("An error occurred:", str(e))