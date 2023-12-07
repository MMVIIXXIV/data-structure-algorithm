



class DisjointSets:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0]*n
        
        
    def findset(self, u):
        if self.p[u] == u:
            return u
        else:
            self.p[u] = self.findset(self.p[u])
            return self.p[u]

    def union(self, u,v):
        a = self.findset(u)
        b = self.findset(v)
        if self.rank[a] < self.rank[b]:
            self.p[a] = b
        else:
            self.p[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1
    #rank is to make tree shallow so that we can reduce time complexity of searrching the parent node




V,E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

print(edgeList)

def checkConnected(V,E,edgelist):
    dsu=DisjointSets(V) # Create a DisjointSets object with V elements
    for u,v in edgeList: # Union all the vertices connected by edges
        dsu.union(u,v) # making set, if they are connected, they will be in same set\




    #this part is to check if all vertices belong to the same set
    root_set=dsu.findset(0)
    for i in range(1,V):   #start from 1 because rootset in above line is index 0
        if dsu.findset(i) != root_set: # If any vertex is in a different set, the graph is not connected

            return False
    return True




def has_cycle(V, E, edgeList):
    dsu = DisjointSets(V)   #*********************** this line is important , for some rason , without this line, the code will get error******************

    for u, v in edgeList:
        # whether the vertices of each edge are already in the same set. 
        # If they are, it means adding that edge would create a cycle,
        if dsu.findset(u) == dsu.findset(v):   
            return True  # The edge u-v forms a cycle
        dsu.union(u, v)

    return False

if checkConnected(V,E,edgeList):
    print("The graph is connected")
else :
    print("The graph is not connected")

if has_cycle(V,E,edgeList):
    print("There is a circle")
else:
    print("No the graph does not contain any circle")


'''
Worst-Case Scenario:

Worst-case scenario occurs when we have a dense graph with a large number of edges.
In this case, the time complexity is dominated by the union operations in the checkConnected function.
The worst-case time complexity of a single union operation is O(n), where n is the number of vertices.
In the worst case, if you have to perform a union for all E edges, the overall time complexity becomes O(E * n).



Normal-Case Scenario:

The normal case is a balanced scenario where the graph has a reasonable number of edges relative to the number of vertices (E is not too close to V^2).
In this scenario, the union operations are generally efficient due to union by rank and path compression.
The average time complexity for each union operation is amortized O(log n).
In the normal case, the overall time complexity is typically O(E * log(n)).



Best-Case Scenario:

The best-case scenario is when the graph is very sparse, and E is much smaller than V^2.
In this case, the union operations are still efficient, but there are fewer of them.
The best-case time complexity is still O(E * log(n)), but with a smaller constant factor compared to the normal and worst cases.
In summary:

Worst-Case Time Complexity: O(E * n)
Normal-Case Time Complexity: O(E * log(n))
Best-Case Time Complexity: O(E * log(n))


'''
'''
The graph will only show connected if all the nodes are connected with a line
'''
