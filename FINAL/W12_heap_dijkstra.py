print("this is 1 based")
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


import sys


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

# for t in list(zip(range(1,V+1),Shortest_Estimate, Parent)):
#     print(*t)
print("Shortest distances from the starting vertex (1):")
print("Vertex\tDistance\tShortest Path")

for i, (dist, parent) in enumerate(zip(Shortest_Estimate, Parent)):
    if parent is not None:
        path = f"{parent} -> {i + 1}"
    else:
        path = str(i + 1)
    
    print(f"{i + 1}\t{dist}\t\t{path}")


'''
This code implements Dijkstra's algorithm to find the shortest paths from a starting vertex to all other vertices in a weighted graph. Here's a step-by-step explanation of the code:

A Heap class is defined to handle the min-heap data structure. It includes methods like insert, extract, heapify, and buildHeap for heap operations. A custom comparison function can also be provided for comparisons.

The graph_type is read from the input, which indicates whether the graph is directed or undirected.

The number of vertices (V) and edges (E) are read from the input.

An adjacency list adj_list is created to represent the graph. Each entry in adj_list is a list of tuples, where each tuple represents an edge from one vertex to another along with its weight.

The code defines a HeapNode class to represent nodes in the min-heap. A HeapNode stores the vertex, its key (shortest estimate), and its parent.

The Dijkstra function implements Dijkstra's algorithm:

Initialize arrays to keep track of visited vertices (S), parents (Parent), and shortest estimates (Shortest_Estimate).
Create a min-heap (PQ) to manage vertices with the smallest tentative distance.
Start with the initial vertex (provided as input).
Continue to extract vertices from the min-heap:
Mark the vertex as visited (in set S).
Update the shortest estimate and parent for the neighbors of the current vertex.
Insert the neighbors into the min-heap with updated estimates if a shorter path is found.
After running Dijkstra's algorithm, the code prints the shortest distances from the starting vertex to all other vertices.
If a vertex is not reachable from the starting vertex, its distance is set to "inf," and its parent is set to None.

The code also adjusts vertex numbers (adding 1) to match the 1-based indexing for output.

The output includes each vertex's number, its shortest estimate, and its parent in the shortest path.

The time complexity of Dijkstra's algorithm using a min-heap is O((V + E) * log(V)), where V is the number of vertices and E is the number of edges in the graph.
 It efficiently finds the shortest paths from a starting vertex to all other vertices in a weighted graph
'''



'''Best Case: If the graph is a dense graph with a large number of edges, the best-case time complexity can be as low as O(|V|^2) when implemented with an adjacency matrix, where |V| is the number of vertices.

Average Case: The average-case time complexity is typically O(|E| + |V| * log(|V|)) when implemented with a priority queue (min heap), where |E| is the number of edges, and |V| is the number of vertices.
 In most practical cases, it's close to O(|E| + |V| * log(|V|).

Worst Case: In the worst case, the time complexity of Dijkstra's algorithm is O(|E| + |V| * log(|V|)), which occurs when the graph is dense with many edges. The priority queue operations dominate the time complexity.'''


''' example test case
Directed Graph
6 15
3 2 20
6 4 22
2 1 7
3 2 17
2 6 1
4 6 20
6 5 27
5 4 30
4 2 25
1 3 25
5 3 3
6 5 1
4 1 14
3 6 1
3 5 10'''