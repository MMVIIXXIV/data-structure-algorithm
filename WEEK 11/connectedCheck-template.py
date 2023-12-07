V,E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

from disjointsets3 import DisjointSets

s = DisjointSets(V)
dsu=DisjointSets(V) 
for u,v in edgeList: 
    dsu.union(u,v) 


flag=True
root_set=dsu.findset(0)
for i in range(1,V):  
    if dsu.findset(i) != root_set: 
        flag=False

print("The graph is connected ") if flag else print("The graph is not connnected")
    