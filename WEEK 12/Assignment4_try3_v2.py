import sys;

def dijkstar_shortest_path(graph,start,end):

    distances = {node : sys.maxsize for node in range(1,N+1)}
    distances[start]=0


    unvisited_nodes=list(range(1,N+1))

    while unvisited_nodes:
        #finding the node with minimal distance
        min_node = None
        for node in unvisited_nodes:
            if min_node is None or distances[ node] < distances[min_node]:
                min_node = node

        # stop if the minimal node is the destination node
        if min_node == end :
            break

        #removing the visited nodes
        unvisited_nodes . remove(min_node)

        #relaxing, updating distances to adjacaent nodes
        for neighbor, weight in graph[min_node]:
            if distances[min_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[min_node ]+ weight
                
    return distances[end]


N,M = map(int,input().split())
graph= {i: [] for i in range(1,N+1)}

for _ in range(M):
    a,b,c = map(int,input().split())
    graph [ a].append((b,c))


x=1
shortest_path_between_two_nodes = dijkstar_shortest_path(graph=graph,start=x,end=N)
print(shortest_path_between_two_nodes)