import sys

def dijkstar_shortest_path(graph, start, end, N):
    distances = {node: sys.maxsize for node in range(1, N + 1)}
    distances[start] = 0
    unvisited_nodes = list(range(1, N + 1))

    while unvisited_nodes:
        # Finding the node with minimal distance
        min_node = None
        for node in unvisited_nodes:
            if min_node is None or distances[node] < distances[min_node]:
                min_node = node

        # Stop if the minimal node is the destination node
        if min_node == end:
            break

        # Removing the visited nodes
        unvisited_nodes.remove(min_node)

        # Relaxing, updating distances to adjacent nodes
        for neighbor, weight in graph[min_node]:
            if distances[min_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[min_node] + weight

    return distances[end]

# Input: Number of vertices (N), number of edges (M)
N, M = map(int, input("Enter the number of vertices (N) and edges (M): ").split())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b, c = map(int, input("Enter edge (a b c): ").split())
    # a-=1
    # b-=1
    graph[a].append((b, c))

start_vertex = int(input("Enter the start vertex: "))
end_vertex = int(input("Enter the end vertex: "))

shortest_path_distance = dijkstar_shortest_path(graph, start_vertex, end_vertex, N)

if shortest_path_distance == sys.maxsize:
    print(f"There is no path from vertex {start_vertex} to {end_vertex}.")
else:
    print(f"Shortest path from vertex {start_vertex} to {end_vertex}: {shortest_path_distance}")


'''
example input 
4 5
1 2 2
1 3 3
2 4 5
3 4 1
4 2 4
'''


#Best Case: O(E + VlogV) when using a binary heap or Fibonacci heap for the priority queue. This occurs when the graph is sparse (few edges) and efficient data structures are used for priority queue operations.

# Average Case: O(E + VlogV) when using efficient priority queue data structures, similar to the best case. 
# This is the expected time complexity for most practical scenarios.

# Worst Case: O(V^2) when using an array-based implementation for the priority queue, and O(V^3) when using a nested loop approach to extract the minimum distance
# . This worst case occurs when the priority queue operations are not optimized, and Dijkstra's algorithm has to search through all vertices in each iteration.

# In practice, Dijkstra's algorithm is often implemented using data structures like binary heaps, Fibonacci heaps, or other priority queue implementations that keep the time complexity within the best or average-case bounds.
#  The choice of data structures significantly impacts the efficiency of the algorithm.
#  Therefore, it is important to use efficient priority queues to ensure that the algorithm performs well, particularly for large and dense graphs.


'''
example case:
Enter the number of vertices (N) and edges (M): 6 15
Enter edge (a b c): 3 2 20
Enter edge (a b c): 6 4 22
Enter edge (a b c): 2 1 7
Enter edge (a b c): 3 2 17
Enter edge (a b c): 2 6 1
Enter edge (a b c): 4 6 20
Enter edge (a b c): 6 5 27
Enter edge (a b c): 5 4 30
Enter edge (a b c): 4 2 25
Enter edge (a b c): 1 3 25
Enter edge (a b c): 5 3 3
Enter edge (a b c): 6 5 1
Enter edge (a b c): 4 1 14
Enter edge (a b c): 3 6 1
Enter edge (a b c): 3 5 10
Enter the start vertex: 1
Enter the end vertex: 6
Shortest path from vertex 1 to 6: 26'''



'''
Certainly, I'll explain Dijkstra's algorithm step by step:

**Dijkstra's Algorithm:**

Dijkstra's algorithm is a greedy algorithm used to find the shortest path from a starting node to all other nodes in a weighted graph. It operates by iteratively selecting the node with the smallest known distance (so far) and relaxing its edges to update the distances to its neighbors.

1. **Initialization:**
   - Create a set of unvisited nodes. Initially, all nodes are unvisited.
   - Initialize a dictionary to store the minimum distance from the starting node to each node. Set the distance of the starting node to 0 and all other nodes to positive infinity.
   - The algorithm selects nodes with the smallest known distance, so it uses a priority queue or a min-heap to efficiently find the node with the minimum distance.

2. **Main Loop:**
   - While there are unvisited nodes:
     - Select the unvisited node with the smallest known distance (from the set of unvisited nodes). Initially, the starting node has a distance of 0.
     - Mark the selected node as visited (remove it from the set of unvisited nodes).
     - For the selected node, consider all of its unvisited neighbors and calculate their tentative distances from the starting node. Update the distances if a shorter path is found.

3. **Relaxation Step:**
   - For each unvisited neighbor of the selected node:
     - Calculate the tentative distance to the neighbor by summing the distance to the selected node and the edge weight from the selected node to the neighbor.
     - If the tentative distance is less than the current assigned distance to the neighbor, update the distance.

4. **Termination:**
   - When all nodes have been visited (or the destination node is reached), the algorithm terminates. The minimum distance from the starting node to all other nodes has been found.

5. **Shortest Path:**
   - To find the shortest path from the starting node to any other node, you can backtrack from the destination node using the recorded distances and predecessors.

**Termination:**
Dijkstra's algorithm terminates when all nodes are visited (if you want to find the shortest path to all nodes) or when the destination node is visited (if you want to find the shortest path to a specific node).

**Time Complexity:**
The time complexity of Dijkstra's algorithm depends on the implementation. With a min-heap or priority queue, the time complexity is typically O(E + V log V), where E is the number of edges, and V is the number of vertices. If an array-based priority queue is used, it can be O(V^2) in the worst case.

The algorithm is efficient for sparse graphs (where E is much less than V^2) and can handle negative edge weights as long as there are no negative weight cycles.

The steps above outline the core principles of Dijkstra's algorithm for finding the shortest path in a weighted graph. It's a versatile algorithm widely used in applications like routing, network optimization, and more.
'''



'''Relaxation is a fundamental concept in algorithms for finding shortest paths in graphs, such as Dijkstra's algorithm. It refers to the process of updating (or improving) the distance or cost associated with a vertex in a graph when a shorter path to that vertex is discovered. The goal of relaxation is to iteratively find the shortest paths from a source vertex to all other vertices in the graph.

Here's how the relaxation process works step by step:

1. **Initialization:** Initially, all vertices are assigned a tentative (initial) distance value, typically set to infinity, except for the source vertex, which is set to zero.

2. **Exploration:** The algorithm explores vertices and edges in the graph to determine if there are shorter paths to other vertices from the source.

3. **Relaxation Step:** When the algorithm examines an edge from one vertex to another, it checks if the currently known distance to the destination vertex can be improved by considering the edge weight.
 If the sum of the distance from the source vertex to the current vertex (the "tentative" distance) and the weight of the edge to the destination vertex is less than the currently known distance to the destination vertex,
   the known distance is updated to the shorter value.

4. **Iterative Process:** The relaxation process is repeated for all vertices and edges in the graph until no further improvements can be made.
 This means that the algorithm continues to explore paths, relaxing edges, and updating distances until it finds the shortest paths from the source vertex to all other vertices.

5. **Optimality:** Once the algorithm completes, the distances assigned to each vertex represent the shortest path from the source vertex to that vertex.

Relaxation ensures that the algorithm progressively refines its estimates of the shortest paths, allowing it to discover the true shortest paths by iteratively considering and updating distance values.

In Dijkstra's algorithm, the relaxation process is at the heart of the algorithm's operation.
 It continuously updates distance values while exploring vertices, ensuring that the final distances stored in the data structure represent the shortest paths from the source vertex to all other vertices in the graph.
   Relaxation is also a key concept in other algorithms for finding shortest paths, like the Bellman-Ford algorithm.'''