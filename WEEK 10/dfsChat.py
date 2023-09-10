
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)

    for next_vertex in graph[start] - visited:
        dfs(graph, next_vertex, visited)
    
    return visited

def main():
    graph_type = input()
    if graph_type != "Directed Graph":
        print("DFS only works on Directed Graph")
        exit()

    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V)]

    for _ in range(E):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj_list[u].append(v)

    color = ["WHITE"] * V
    p = [None] * V
    d = [-1] * V
    f = [-1] * V

    time = 0
    visited = set()

    for vertex in range(V):
        if vertex not in visited:
            visited = dfs(adj_list, vertex, visited)

    for v in range(V):
        if d[v] == -1:
            dv = "undiscovered"
        else:
            dv = d[v]
        
        if f[v] == -1:
            fv = ""
        else:
            fv = f[v]
        
        if p[v] is not None:
            pv = p[v] + 1
        else:
            pv = "None"

        print("%d %5s %s %s %s" % (v + 1, color[v], dv, fv, pv))

if __name__ == "__main__":
    main()
