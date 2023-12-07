# Undirected Graph:

# Vertices: A, B, C, D
# Edges: (A, B), (A, C), (B, C), (B, D), (C, D)


# Adjacency List:
# In an adjacency list representation, we associate each vertex with a list of its neighboring vertices.

# A: [B, C]
# B: [A, C, D]
# C: [A, B, D]
# D: [B, C]



# Adjacency Matrix:
# In an adjacency matrix representation, we use a 2D matrix to indicate whether there is an edge between two vertices.
#  A value of 1 represents an edge, and 0 represents no edge.
#there is code which can make matric in week 9 

#    A  B  C  D
# A  0  1  1  0
# B  1  0  1  1
# C  1  1  0  1
# D  0  1  1  0

'''
4
0 1 0 1
1 0 1 0
0 0 1 0
1 1 0 0'''

# Edge List:
# In an edge list representation, we list all the edges in the graph as pairs of vertices.
# (A, B)
# (A, C)
# (B, C)
# (B, D)
# (C, D)



def create_adjacency_list(vertices, edges):
    adj_list = [[] for _ in range(vertices)]
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)  # For an undirected graph
    return adj_list

def create_adjacency_matrix(vertices, edges):
    adj_matrix = [[0] * vertices for _ in range(vertices)]
    for edge in edges:
        u, v = edge
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1  # For an undirected graph
    return adj_matrix

# Input
vertices, edges_count = map(int, input("Enter the number of vertices and edges (e.g., '4 5'): ").split())
edges = []

print("Enter the edges (format: 'u v' without quotes, one per line):")
for _ in range(edges_count):
    u, v = map(int, input().split())
    edges.append((u, v))

# Create representations
adjacency_list = create_adjacency_list(vertices, edges)
adjacency_matrix = create_adjacency_matrix(vertices, edges)
edge_list = edges

# Print representations
print("\nAdjacency List:")
for i, neighbors in enumerate(adjacency_list):
    print(f"{i}: {neighbors}")

print("\nAdjacency Matrix:")
for row in adjacency_matrix:
    print(" ".join(map(str, row)))

print("\nEdge List:")
for edge in edge_list:
    print(f"({edge[0]}, {edge[1]})")
