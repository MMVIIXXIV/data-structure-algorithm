import heapq

# Define constants
INF = float('inf')

# Read input
N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b, c))

# Dijkstra's algorithm
dist = [INF] * N
dist[0] = 0

pq = [(0, 1)]  # Priority queue (distance, vertex)
while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u - 1]:
        continue
    for v, w in graph[u - 1]:
        if dist[u - 1] + w < dist[v - 1]:
            dist[v - 1] = dist[u - 1] + w
            heapq.heappush(pq, (dist[v - 1], v))

# Output the shortest distance to vertex N
print(dist[N - 1])
