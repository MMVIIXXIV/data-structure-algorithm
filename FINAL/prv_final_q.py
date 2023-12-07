def find_smallest_gap(edges, k):
    # Helper function to find the root of a set (used for checking connectivity)
    def find_root(parents, node):
        if parents[node] == node:
            return node
        return find_root(parents, parents[node])

    # Sort the edges by weight in non-decreasing order
    edges.sort(key=lambda x: x[2])

    n = len(edges)
    parents = list(range(n))  # Initialize each vertex as its own cluster
    num_clusters = n  # Start with n clusters

    for edge in edges:
        u, v, weight = edge
        root_u = find_root(parents, u)
        root_v = find_root(parents, v)

        if root_u != root_v:  # If u and v are not in the same cluster
            parents[root_u] = root_v  # Union the clusters by setting a parent
            num_clusters -= 1

        if num_clusters == k:  # Stop when we have k clusters
            break

    smallest_gap = float('inf')

    # Iterate through the remaining edges and find the smallest gap
    for edge in edges:
        u, v, weight = edge
        root_u = find_root(parents, u)
        root_v = find_root(parents, v)

        if root_u != root_v:  # If u and v are in different clusters
            smallest_gap = min(smallest_gap, weight)

    return smallest_gap

# Read input
n, m = map(int, input().split())  # Number of vertices and edges
edges = [list(map(int, input().split())) for _ in range(m)]  # Edge list
k = int(input())  # Number of clusters

result = find_smallest_gap(edges, k)
print(result)
