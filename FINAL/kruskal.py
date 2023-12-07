class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def kruskal(self):
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [i for i in range(self.V)]
        result = []
        i = 0
        e = 0

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, x, y)

        print("Edges in the Minimum Spanning Tree:")
        for u, v, w in result:
            print(f"{u} - {v} : {w}")

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, x, y):
        x_set = self.find(parent, x)
        y_set = self.find(parent, y)
        parent[x_set] = y_set


# Input format: V (number of vertices), E (number of edges)
V, E = map(int, input().split())
g = Graph(V)

# Input format: E lines of edges (u, v, w)
for _ in range(E):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

g.kruskal()
