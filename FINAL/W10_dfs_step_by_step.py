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

    print(f"Start {chr(65 + u)}")
    print(f"Discovery Time {chr(65 + u)} (D-{time})")

    discovered_nodes = []

    for v in adj_list[u]:
        if color[v] == "WHITE":
            p[v] = u
            discovered_nodes.append(chr(65 + v))

    if discovered_nodes:
        print(f"Discovered {', '.join(discovered_nodes)}")

    for v in adj_list[u]:
        if color[v] == "WHITE":
            dfs_visit(v)

    color[u] = "BLACK"
    time += 1
    f[u] = time

    print(f"Finishing Time {chr(65 + u)} (F-{time})")
    print(f"Retract {chr(65 + u)})")


# Start DFS from a specific vertex, for example, vertex 1
start_vertex = int(input("Enter the starting vertex for DFS (1 to N): "))
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
