# Provided topological_sort function
visited = []
stack = []

def DFS_visit(s, adj):
    global visited, stack
    
    for v in adj[s]:
        if not visited[v]:
            visited[v] = True
            DFS_visit(v, adj)
    stack.append(s)

def topological_sort(V, adj):
    global visited, stack
    
    visited = [False]*V
    for s in range(V):
        if not visited[s]:
            visited[s] = True
            DFS_visit(s, adj)
    stack.reverse()
    return stack

# Main code
V, E = map(int, input().split())
adjacency_list = [[] for _ in range(V)]

for _ in range(E):
    s, t = map(int, input().split())
    adjacency_list[s].append(t)

sorted_vertices = topological_sort(V, adjacency_list)

for vertex in sorted_vertices:
    print(vertex)
