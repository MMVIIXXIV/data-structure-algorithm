
print("this is one based")
graph_type = input()
if graph_type != "Directed Graph" and graph_type != "Undirected Graph":
    print("Graph type should be 'Directed Graph' or 'Undirected Graph'.")
    exit()

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
p = [None] * V
time = 0
d = [-1] * V
f = [-1] * V

# Write your Depth-First Search code below
# Don't forget to make the initial dfs call! :)


def dfs_visit(u):
    global time
    time += 1
    d[u] = time
    color[u] = "GRAY"

    for v in adj_list[u]:
        if color[v] == "WHITE":
            p[v] = u
            dfs_visit(v)

    color[u] = "BLACK"
    time += 1
    f[u] = time


# Start DFS from a specific vertex, for example, vertex 1
start_vertex = int(input("Enter the starting vertex for DFS: "))
dfs_visit(start_vertex - 1)  # Adjusting for 0-based indexing

# Then continue with the loop for any remaining undiscovered nodes
for v in range(V):
    if color[v] == "WHITE":
        dfs_visit(v)

# Print output with clearer formatting
print("Vertex Color   Discovery Time Finish Time Parent")
for v in range(V):
    color_label = color[v]
    discovery_time = d[v]
    finish_time = f[v]
    parent_label = "None" if p[v] is None else str(p[v] + 1)

    print(f"{v + 1:6d} {color_label:7s} {discovery_time:14d} {finish_time:11d} {parent_label}")


'''

example input 
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



Directed Graph
4 5
1 2
2 4
3 4
2 1
3 3
'''
#Theory of Depth-First Search (DFS):


# Depth-First Search is a graph traversal algorithm used to explore and analyze the structure of a graph.
#  It operates by visiting a starting node and then recursively exploring as far as possible along each branch before backtracking.
#  Here are the key concepts and steps involved in DFS:


# Initialization:

# Start from a chosen node in the graph. This node is marked as "visited."
# Initialize data structures to keep track of visited nodes, discovery times, and finish times.
# Exploration:

# For the current node, explore its neighbors. If a neighbor is unvisited, mark it as "visited" and consider it for further exploration.
# Continue this process recursively, diving deeper into the graph.
# Backtracking:

# If there are no unvisited neighbors left for a node, backtrack to the previous node to explore other branches.
# This process continues until all nodes in the connected component have been visited.
# Recording Information:

# During the traversal, record information about each node:
# Color: Tracks the state of the node (WHITE for unvisited, GRAY for visiting, BLACK for visited).
# Discovery Time: The timestamp when the node is first encountered during the traversal.
# Finish Time: The timestamp when the traversal finishes exploring the node.
# Parent: The parent node in the DFS traversal tree.
# Traversal Trees:

# DFS forms a traversal tree from the starting node, where each node becomes a parent or child of another node based on their traversal order.
# This traversal tree helps in understanding the relationships and structure of the graph.



























'''Time Complexity of DFS:

The time complexity of DFS depends on the number of vertices (V) and edges (E) in the graph. In general, the time complexity is O(V + E) in all cases.

Best Case: In the best case, when the graph is a simple linear chain, DFS still explores each vertex and edge once, resulting in O(V + E) time complexity.

Average Case: In the average case, where the graph is not overly structured, DFS still explores each vertex and edge once, resulting in O(V + E) time complexity.

Worst Case: In the worst case, when the graph is a complete graph (every vertex connected to every other vertex), DFS explores each vertex and edge once, resulting in O(V + E) time complexity.
DFS operates by visiting every vertex and edge once, and the time complexity is linear in terms of the size of the graph (V + E).
 It efficiently traverses the graph to find connected components, cycles, and other structural information.'''

















'''
Depth-First Search (DFS) is a graph traversal algorithm that explores a graph by visiting as far as possible along each branch before backtracking. It is commonly used to explore and analyze the structure of a graph. Let's break down the code step by step and explain the theory behind each part:





**Step 1: Input and Graph Type Validation**
```python
graph_type = input()
if graph_type != "Directed Graph" and graph_type != "Undirected Graph":
    print("Graph type should be 'Directed Graph' or 'Undirected Graph'.")
    exit()
```

- In this step, the code first asks the user to specify the type of graph: either "Directed Graph" or "Undirected Graph."
- It performs a check to ensure that the specified graph type is valid. If not, it prints an error message and exits.




**Step 2: Graph Initialization**
```python
V, E = map(int, input().split())
adj_list = [[] for v in range(V)]
for i in range(E):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj_list[u].append(v)
    if graph_type == "Undirected Graph":
        adj_list[v].append(u)
```

- In this step, the code takes input for the number of vertices (`V`) and edges (`E`).
- It initializes an adjacency list (`adj_list`) to represent the graph. The list has `V` empty lists to store the neighbors of each vertex.
- It then processes the input for edges and populates the adjacency list. If the graph is undirected, it adds edges in both directions.




**Step 3: Data Structures Initialization**
```python
color = ["WHITE"] * V
p = [None] * V
time = 0
d = [-1] * V
f = [-1] * V
```

- In this step, the code initializes several data structures for tracking the state of nodes during the DFS traversal:
  - `color`: An array to track the color of each node (WHITE for unvisited, GRAY for visiting, and BLACK for visited).
  - `p`: An array to store the parent of each node in the DFS tree.
  - `time`: A variable to keep track of time, which is used for discovery and finish times.
  - `d`: An array to store the discovery time for each node.
  - `f`: An array to store the finish time for each node.




**Step 4: DFS Algorithm Implementation**
```python
def dfs_visit(u):
    global time
    time += 1
    d[u] = time
    color[u] = "GRAY"
    
    for v in adj_list[u]:
        if color[v] == "WHITE":
            p[v] = u
            dfs_visit(v)
    
    color[u] = "BLACK"
    time += 1
    f[u] = time
```

- This step defines the DFS traversal logic. It uses a recursive approach to explore the graph.
- The `dfs_visit` function is called for each unvisited node. Inside the function:
  - Time is incremented, and the discovery time (`d`) for the node is recorded.
  - The color of the node is changed to "GRAY" to mark it as currently visiting.
  - For each unvisited neighbor (`v`) of the current node (`u`), the function is called recursively.
  - The parent of each neighbor is updated to be the current node.
  - After exploring all neighbors, the node's color is changed to "BLACK" to mark it as fully visited, and the finish time (`f`) is recorded.
  


**Step 5: Starting DFS from Each Undiscovered Node**
```python
for v in range(V):
    if color[v] == "WHITE":
        dfs_visit(v)
```

- This step starts DFS from each undiscovered node in the graph. It iterates through all nodes (`v`),
 and if a node is unvisited (color is "WHITE"), it calls `dfs_visit(v)` to start the DFS traversal from that node.

 

**Step 6: Output Printing**
```python
print("Vertex Color   Discovery Time Finish Time Parent")
for v in range(V):
    color_label = color[v]
    discovery_time = d[v]
    finish_time = f[v]
    parent_label = "None" if p[v] is None else str(p[v] + 1)

    print(f"{v + 1:6d} {color_label:7s} {discovery_time:14d} {finish_time:11d} {parent_label}")
```

- This step prints the output in a well-formatted manner. It displays information for each vertex:
  - Vertex number (`v + 1`)
  - Color (WHITE, GRAY, or BLACK)
  - Discovery time
  - Finish time
  - Parent (either a number or "None" if there is no parent)

The result is a clear and informative output that helps you understand the DFS traversal of the graph, including when nodes are discovered and finished.
'''