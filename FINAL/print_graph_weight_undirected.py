import networkx as nx
import matplotlib.pyplot as plt

# Main code
V, E = map(int, input().split())
adjacency_list = [[] for _ in range(V)]

for _ in range(E):
    s, t, w = map(int, input().split())
    s-=1
    t-=1
    adjacency_list[s].append((t, w))
    adjacency_list[t].append((s, w))  # Undirected graph, so add edges in both directions

# Create an undirected graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(range(V))

# Add edges from adjacency list with weights
for i in range(V):
    for j, w in adjacency_list[i]:
        G.add_edge(i, j, weight=w)

# Draw the graph
pos = nx.spring_layout(G, seed=42)  # You can use different layout algorithms
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black',  font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Undirected Graph with Weights")
plt.show()

# example input
# 4 4 
# 0 1 1 
# 1 2 2
# 1 3 3
# 2 3 3
