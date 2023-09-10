def create_adjacency_matrix(vertices, edges):
    adjacency_matrix = [[0] * vertices for _ in range(vertices)]
    for _ in range(edges):
        source, target = map(int, input("Enter edge (source target): ").split())
        adjacency_matrix[source][target] = 1
        adjacency_matrix[target][source] = 1  # Assuming an undirected graph
    return adjacency_matrix

def print_adjacency_matrix(adjacency_matrix):
    print("Adjacency Matrix:")
    for row in adjacency_matrix:
        print(" ".join(map(str, row)))

def main():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))
    
    adjacency_matrix = create_adjacency_matrix(vertices, edges)
    print_adjacency_matrix(adjacency_matrix)

if __name__ == "__main__":
    main()
