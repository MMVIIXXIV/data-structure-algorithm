
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





V,E = map (int,input().split())
edgelist=[]
for i in range(E):
    edgelist.append(tuple(map(int,input().split())))

s= DisjointSets(V)
for u,v in edgelist:
    s.union(u,v)
flag = True
root_set = s.findset(0)
for i in range(1,V):
    if s.findset(i) != root_set:
        flag= False


print("The graph is connected ") if flag else print("The graph is not connnected")
    

'''example case 
6 10
2 6
5 3
5 6
3 4
5 1
3 6
1 4
4 2
3 1
6 1

'''
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

