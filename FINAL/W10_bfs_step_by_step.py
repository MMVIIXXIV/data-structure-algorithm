from collections import defaultdict, deque
print("this is one based")
# Function to perform BFS
def bfs(adj_list, start_node):
    # Initialize colors and the queue.
    colors = defaultdict(lambda: 'white')
    queue = deque()

    # Start from the initial node.
    queue.append(start_node)
    colors[start_node] = 'gray'

    while queue:
        level_size = len(queue)  # Number of nodes at the current level.
        
        for _ in range(level_size):
            current_node = queue.popleft()
            print(f'Node {current_node + 1} is {colors[current_node]}')

            for neighbor in adj_list[current_node]:
                if colors[neighbor] == 'white':
                    print(f'  Discovered neighbor {neighbor + 1}')
                    queue.append(neighbor)
                    colors[neighbor] = 'gray'
                    print(f'  Node {neighbor + 1} is {colors[neighbor]}')

            colors[current_node] = 'black'
            print(f'Node {current_node + 1} is {colors[current_node]}')

        if queue:
            print("Transition to the next level of nodes.")

# Input
V, E = map(int, input().split())
adj_list = [[] for v in range(V)]

for _ in range(E):
    u, v = map(int, input().split())
    adj_list[u - 1].append(v - 1)
    adj_list[v - 1].append(u - 1)

start_node = int(input("Enter the starting node for BFS: ")) - 1

# Start the BFS
bfs(adj_list, start_node)
