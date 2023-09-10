graph_type = input()
V,E = map(int, input().split())
adj_list = [[] for v in range(V)]
 
for i in range(E):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    # print(adj_list)
    adj_list[u].append(v)
    # print(adj_list)
    if graph_type == "Undirected Graph":
        adj_list[v].append(u)

color = ["WHITE"]*V
d = [-1]*V
p = [None]*V

# Write your Breast-First Search code below

visited=[]
queue=[]
def bfs(graph, start):
    visited.append(start)
    queue.append(start)
    d[start] = 0

    while queue:
        s = queue.pop(0)
        for neighbour in graph[s]:
            if color[neighbour] == "WHITE":
                visited.append(neighbour)
                queue.append(neighbour)
                color[neighbour] = "GRAY"
                d[neighbour] = d[s] + 1
                p[neighbour] = s

        color[s] = "BLACK"
for v in range(V):
    if color[v] == "WHITE":
        bfs(adj_list, v)



# The code below is for printing output

for v in range(V):
    if d[v] == -1:
        dv = "Inf"
    else:
        dv = d[v]
    if p[v] != None:
        pv = p[v]+1
    else:
        pv = "None"

    print("%d %5s" % (v+1, color[v]), dv, pv)
    

