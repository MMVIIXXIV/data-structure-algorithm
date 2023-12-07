class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def kruskal(V, edges):
    edges.sort(key=lambda edge: edge[2])  # Sort edges by weight
    mst = []
    total_length = 0  # Initialize total length to 0
    disjoint_set = DisjointSet(V)

    for edge in edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            mst.append((u, v, weight))
            total_length += weight  # Add the edge's weight to the total length
            disjoint_set.union(u, v)

    return mst, total_length  # Return both the MST and total length

# Input
# 
print("this is one based")
V, E = map(int, input().split())
edges = []
for i in range(E):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    edges.append((u, v, w))

# Find MST using Kruskal's algorithm
minimum_spanning_tree, mst_length = kruskal(V, edges)

# Output the MST
print("Minimum Spanning Tree (Edges):")
for edge in minimum_spanning_tree:
    u, v, weight = edge
    print(f"{u + 1} - {v + 1} (Weight: {weight}")
print(f"Total Length of MST: {mst_length}")