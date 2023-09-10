# Function to perform Depth-First Search (DFS) on a directed graph
def depth_first_search(graph, current_node, visited_nodes):
    # Mark the current node as visited
    visited_nodes[current_node] = True
    
    # Print the current node
    print("Visiting node:", current_node)
    
    # Explore each neighbor of the current node
    for neighbor in graph[current_node]:
        if not visited_nodes[neighbor]:
            # Recursively perform DFS on unvisited neighbors
            depth_first_search(graph, neighbor, visited_nodes)

# Input: Number of edges and vertices
num_edges, num_vertices = map(int, input().split())

# Initialize an adjacency list to represent the directed graph
adjacency_list = [[] for _ in range(num_vertices)]

# Build the graph by adding edges
for _ in range(num_edges):
    source, destination = map(int, input().split())
    source -= 1  # Adjust for 1-based indexing
    destination -= 1  # Adjust for 1-based indexing
    adjacency_list[source].append(destination)

# Initialize an array to keep track of visited nodes
visited = [False] * num_vertices

# Perform DFS from each unvisited node
for node in range(num_vertices):
    if not visited[node]:
        print("Starting DFS from node:", node)
        depth_first_search(adjacency_list, node, visited)
