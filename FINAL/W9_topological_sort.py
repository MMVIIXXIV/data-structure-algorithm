# Provided topological_sort function
print("this is zero based")
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


'''Topological Sort Function (topological_sort):

The code defines a topological_sort function that performs topological sorting using Depth-First Search (DFS).
It initializes a list called visited to keep track of visited nodes and an empty stack to store the topological order.
The function takes the number of vertices (V) and an adjacency list (adj) as inputs.
Depth-First Search (DFS_visit):

The code defines a DFS_visit function that implements DFS to explore the graph and build the topological order.
It takes a source vertex s and the adjacency list adj as inputs.
Within DFS_visit, it iterates through the neighbors of the source vertex and recursively explores unvisited neighbors.
When all neighbors are explored, the source vertex s is appended to the stack.
Main Code:

In the main code, it reads the number of vertices (V) and edges (E) from the user.
It initializes an empty adjacency list adjacency_list to represent the graph.
It then reads the edges from the user input and populates the adjacency list accordingly.
Sorting and Printing:

After constructing the adjacency list, the code calls the topological_sort function with V and adjacency_list as arguments.
The result of the topological sort is stored in sorted_vertices.
Finally, the code prints the sorted vertices.
This code follows the standard approach for topological sorting using DFS and adjacency lists. \
It explores the graph while maintaining a visited list and a stack to store vertices in the correct order.
 The order in which the vertices are pushed onto the stack in the DFS_visit function corresponds to a topological sort.

However, it is important to note that this code assumes that the input graph is a valid directed acyclic graph (DAG).
If the input graph contains cycles, this code may not produce a valid topological sort.
Therefore, it's essential to ensure that the input graph is indeed a DAG for this code to work correctly.'''




# Best Case:

# In the best case scenario, the graph is a relatively simple DAG with a small number of vertices and edges.
# The best case occurs when the graph is already in topological order or nearly so,
#  and the DFS traversal doesn't need to backtrack much.

# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
# Explanation: In this case, the DFS traversal may visit each vertex and edge once
# , resulting in a linear time complexity.



# Average Case:
# The average case assumes a typical scenario for topological sorting,
#  where the graph is a DAG, but the order of vertices is not already sorted optimally.
#  There may be some backtracking involved in the DFS traversal.

# Time Complexity: O(V + E)
# Explanation: In the average case, the DFS traversal still visits each vertex and edge once. It is still linear in terms of the number of vertices and edges.
# Worst Case:





# The worst case
#  occurs when the graph is a long linear chain,
#  and the DFS traversal has to backtrack extensively.
#  In this case, the algorithm may take more time.

# Time Complexity: O(V + E)
# Explanation: Even in the worst case, where there's significant backtracking,
#  the DFS traversal is still bounded by O(V + E).
#  This is because, in a valid DAG, there can be at most V vertices and E edges.
# Overall, the time complexity of the provided topological sorting code is linear, O(V + E), in all cases.
# This is because it uses a depth-first search (DFS) algorithm to explore the graph, and the DFS algorithm's time complexity is linear in terms of the number of vertices and edges in the graph.