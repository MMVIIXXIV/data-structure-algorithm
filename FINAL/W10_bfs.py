graph_type = input()
V, E = map(int, input().split())
adj_list = [[] for v in range(V)]

for i in range(E):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj_list[u].append(v)
    if graph_type == "Undirected Graph":
        adj_list[v].append(u)

color = ["WHITE"] * V
d = [-1] * V
p = [None] * V

# Function to perform BFS
visited = []
queue = []

def bfs(graph, start):
    visited.append(start)
    queue.append(start)
    d[start] = 0

    while queue:
        s = queue.pop(0)
        for neighbour in graph[s]:
            if color[neighbour] == "WHITE":
                visited.append(neighbour)
                queue.append(neighbour)
                color[neighbour] = "GRAY"
                d[neighbour] = d[s] + 1
                p[neighbour] = s

        color[s] = "BLACK"

# Choose a starting node (e.g., 0) for BFS
start_node = int(input("Enter the starting node for BFS: ")) - 1

# Run BFS from the chosen starting node
bfs(adj_list, start_node)

# Print the distances and parents
for v in range(V):
    if d[v] == -1:
        dv = "Inf"
    else:
        dv = d[v]
    if p[v] is not None:
        pv = p[v] + 1
    else:
        pv = "None"

    print(f"{v + 1} {color[v]} {dv} {pv}")


'''Input:

The code first takes input for the type of graph ("Directed Graph" or "Undirected Graph").
It also takes the number of vertices (V) and edges (E) in the graph.
Building the Adjacency List:

It constructs an adjacency list (adj_list) for the graph, which represents the structure of the graph as a list of lists.
It reads and processes the edges provided by the user.
If the graph is undirected, it adds edges in both directions (i.e., for an edge u-v, it adds both u->v and v->u).
Initialization:

It initializes data structures:
color: An array representing the state of each vertex in the BFS traversal (WHITE for unvisited, GRAY for being processed, and BLACK for fully processed).
d: An array to store the distance from the chosen starting node to each vertex. It's initialized with -1 to indicate that distances are not yet determined.
p: An array to store the parent of each vertex in the BFS tree. It's initialized as None to indicate no parent.
BFS Function (bfs):

The bfs function performs the BFS traversal.
It starts from the chosen starting node and explores the graph in a breadth-first manner.
It uses a queue to manage the order of exploration.
As it explores vertices and their neighbors, it updates the color, distance (d), and parent (p) accordingly.
Choose a Starting Node:

The user is prompted to enter the index of the starting node for BFS. The user can choose any vertex by providing its index.
Run BFS:

The code runs the BFS algorithm starting from the chosen node.
Print Output:

After BFS is completed, the code prints information for each vertex:
Vertex number.
Color (WHITE, GRAY, or BLACK).
Distance (d) from the chosen starting node.
Parent (p) in the BFS tree.'''


# Best Case:

# In the best case, the BFS algorithm completes with minimal exploration, which happens when the starting node is directly connected to all other nodes (a star-shaped graph).

# Time Complexity: O(V + E)
# Explanation: In this case, the BFS explores all vertices and edges once, resulting in a linear time complexity.
# 
# 
# 
# 
# Average Case:
# In the average case, the BFS explores a typical graph, and the starting node may not be directly connected to all other nodes. 
# The graph may be more complex than a star-shaped graph.
# Time Complexity: O(V + E)
# Explanation: The BFS explores all vertices and edges once, leading to a linear time complexity.
#
# 
# 
#  Worst Case:
# The worst case occurs when the BFS explores the entire graph, such as in a completely connected graph or a graph that has a long linear structure.
# Time Complexity: O(V + E)
# Explanation: Even in the worst case, where the BFS explores the entire graph, the time complexity is still O(V + E). This is because BFS visits each vertex and each edge at most once.
#
# 
# 
# The time complexity is O(V + E) in all cases because BFS explores all vertices and edges in the graph, and the time taken to explore each vertex and edge is proportional to their number.
# 
# 
# 
# Therefore, the time complexity remains linear with respect to the number of vertices and edges in the graph.




'''EXAMPLE INPUT
Undirected Graph
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