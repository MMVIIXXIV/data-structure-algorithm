from topological_sort import *

# A call to topological_sort must be with two arguments
# 1) The number of vertices of the Directed Acyclic Graph
# 2) The adjacency list of the graph





def read_input():
    V, E = map(int, input().split())
    adjacency_list = {i: [] for i in range(V)}

    for _ in range(E):
        s, t = map(int, input().split())
        adjacency_list[s].append(t)

    return V, adjacency_list

V, adjacency_list = read_input()

sorted_order = topological_sort(V, adjacency_list)

# Print the result
for vertex in sorted_order:
    print(vertex)