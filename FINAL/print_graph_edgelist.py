# import networkx as nx
# import matplotlib.pyplot as plt

# # Read input
# n, e = map(int, input().split())
# EdgeList = []

# for i in range(e):
#     x = list(map(int, input().split()))
#     EdgeList.append(x)

# # Create a graph
# G = nx.Graph()

# # Add vertices
# for vertex in range(1, n + 1):
#     G.add_node(vertex)

# # Add edges
# for edge in EdgeList:
#     u, v = edge
#     G.add_edge(u, v)

# # Draw and display the graph
# pos = nx.spring_layout(G)  # You can change the layout algorithm as needed
# nx.draw(G, pos, with_labels=True, node_size=300, node_color='skyblue', font_size=10, font_color='black')
# plt.title("Graph Visualization")
# plt.show()
import networkx as nx
import matplotlib.pyplot as plt

# Main code
V, E = map(int, input().split())
adjacency_list = [[] for _ in range(V)]

for _ in range(E):
    s, t, = map(int, input().split())
    s-=1
    t-=1
    adjacency_list[s].append(t)

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_nodes_from(range(V))

# Add edges from adjacency list
for i in range(V):
    for j in adjacency_list[i]:
        G.add_edge(i, j)

# Draw the graph
pos = nx.spring_layout(G, seed=42)  # You can use different layout algorithms
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black', arrows=True)
plt.title("Directed Graph")
plt.show()
