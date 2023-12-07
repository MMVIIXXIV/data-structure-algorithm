import sys
from Heap import *

graph_type = input()
V,E = map(int, input().split())
adj_list = [[] for v in range(V)]
for i in range(E):
    u,v,w = map(int, input().split())
    u, v = u-1, v-1
    adj_list[u].append((v,w))

print(adj_list)

class HeapNode():
    def __init__(self,vertex=None,key=sys.maxsize,parent=None):
        self.key = key
        self.parent = parent
        self.vertex = vertex


def Dijkstra(s): 
    # Start vertex
    S = [False] * V
    Parent = [None] * V
    Shortest_Estimate = [sys.maxsize] * V

    a = HeapNode(s,0,None)
    PQ = heap(cmp=lambda x,y:x.key<y.key) # create minheap
    PQ.insert(a) # insert a
    while not PQ.empty():
        t = PQ.extract()    
        u = t.vertex        
        if S[u] == False:
            S[u] = True
            Shortest_Estimate[u] = t.key

            # just keep updating shortest estimate for each vertex
            for v,w in adj_list[u]:
                if not S[v] and (Shortest_Estimate[u] + w < Shortest_Estimate[v]):
                    a = HeapNode(v,Shortest_Estimate[u] + w,u)
                    Shortest_Estimate[v] = Shortest_Estimate[u] + w
                    Parent[v] = u
                    PQ.insert(a)


    return Shortest_Estimate, Parent

Shortest_Estimate, Parent = Dijkstra(0)
for i in range(len(Parent)):
    if Parent[i] is not None:
        Parent[i] += 1

for t in list(zip(range(1,V+1),Shortest_Estimate, Parent)):
    print(*t)