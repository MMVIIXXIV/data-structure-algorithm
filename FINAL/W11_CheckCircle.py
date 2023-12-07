
print("this is one based")

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

def has_cycle(V, E, edgeList):
    dsu = DisjointSets(V)   #*********************** this line is important , for some rason , without this line, the code will get error******************

    for u, v in edgeList:
        # whether the vertices of each edge are already in the same set. 
        # If they are, it means adding that edge would create a cycle,
        if dsu.findset(u) == dsu.findset(v):   
            return True  # The edge u-v forms a cycle
        dsu.union(u, v)

    return False



V,E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

print(edgeList)
if has_cycle(V,E,edgeList):
    print("There is a circle")
else:
    print("No the graph does not contain any circle")