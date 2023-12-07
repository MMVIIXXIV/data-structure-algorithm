import sys

class heap:


    def compare(x, y):  # a default compare function for min heap
        return x < y


    def empty(self):
        if self.heapsize == 0:
            return True
        else:
            return False


    def insert(self, x):
        self.heapsize += 1
        if len(self.a) < self.heapsize:
            self.a.append(x)
        else:
            self.a[self.heapsize-1] = x
        i = self.heapsize-1
        j = (i-1)//2
        while i > 0 and self.cmp(self.a[i],self.a[j]):
            self.a[i],self.a[j] = self.a[j],self.a[i]
            i = j
            j = (i-1)//2


    def extract(self):
        x = self.a[0]
        last = self.heapsize-1
        self.a[0],self.a[last] = self.a[last],self.a[0]
        self.heapsize -= 1
        self.heapify(0)
        return x


    def heapify(self, i):
        l = i * 2 + 1
        r = (i + 1) * 2
        if l < self.heapsize and self.cmp(self.a[l], self.a[i]):
            largest = l
        else:
            largest = i
        if r < self.heapsize and self.cmp(self.a[r], self.a[largest]):
            largest = r
        if largest != i:
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            self.heapify(largest)

    def buildHeap(self):
        for i in range((self.heapsize-1)//2, -1, -1):
            self.heapify(i)

    def __init__(self, items=[], cmp=compare):
        self.a = items
        self.cmp = cmp
        self.heapsize = len(self.a)
        if len(self.a) > 0:
            self.buildHeap()

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