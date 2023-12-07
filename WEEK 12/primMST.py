import sys
from Heap import *

V,E = map(int, input().split())
adj_list = [[] for v in range(V)]

for i in range(E):
    u,v,w = map(int, input().split())
    adj_list[u].append((v,w))
    adj_list[v].append((u,w))
    #IMPORTANT: Prim's require 2 way connection representation

for each in adj_list:
    print(each)

class HeapNode():
    def __init__(self,vertex=None,key=sys.maxsize,parent=None):
        self.key = key
        self.parent = parent
        self.vertex = vertex


def PrimMST(r):
    MST = [False] * V                                   # create arrays for MST
    MinKey = [sys.maxsize] * V                          # infinity for each MinKey
    total = 0                                           # initialize total as zero

    s = HeapNode(r,0,None)                              
    PQ = heap(cmp=lambda x,y:x.key<y.key)               
    # create heap 
    # function for comparing
    # less than is a min heap
    # x would have more priority than y fs x is less than y
    # the minimum number has the most priority
    PQ.insert(s)


    while not PQ.empty():
        temp = PQ.extract()
        u = temp.vertex
        if MST[u] == False:                              #if unvisited, False in MST list for that u
            total += temp.key                            #add key to total (add weight to total)
            MST[u] = True                                #set visited u to true, True in MST list for that u
            print(f"{u} has been visited", end=": ")
            #print(MST, end=" ")
            for v,w in adj_list[u]:                      #go through other vertices that are adjecent to u and their corresponding weights
                if MST[v] == False and w < MinKey[v]:    #if there are unvisited vertices and weight is less than Minkey for that vertice,
                    s = HeapNode(v,w,u)                  #create HeapNode object s (v for vertex, w for key, current u for parent)
                    MinKey[v] = w                        #update mininum weight for that vertex
                    PQ.insert(s)     
            print(MinKey)                                #insert the created HeapNode object, s, into the priority queue and repeat


    return MinKey, total                                 #return MinWeight for each vertex, and then total minimum weight


print(PrimMST(0))