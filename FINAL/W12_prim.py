


print("this is 1 based-undirected")

graph = input()
V,E = map(int,input().split())
adj_list= [[] for v in range(V)]
for e in range(E):
    start,end,weight = map(int,input().split())
    start ,end = start - 1, end - 1
    adj_list[start]. append((end, weight))



def prim(adj_list):
    V = len(adj_list)
    visited = [False] * V
    key = [ float("inf")] * V
    parent = [ -1] * V

    key [0] = 0 
    for _ in range(V):
        #finding the vertex with the minimum key value


        min_key =  float("inf")
        u = -1
        for v in range(V):
            if not visited [ v ] and key [ v ] < min_key:

                min_key = key [ v ]
                u = v
        
        if u == -1:
            break 

        visited[u]= True

        for neighbors, weight in adj_list[u]:
            if not visited[neighbors] and weight < key [ neighbors ] :
                key [ neighbors ] = weight
                parent [ neighbors ] = u

    total_weight = 0
    for i in range( 1, V):
        total_weight += key[i]
        print(f" Edge {parent[i] + 1} - {i+1 }: Weight {key [ i]} ")
    print(f"Total Weight of MST {total_weight}")



prim(adj_list=adj_list)

















'''

In your input, you specified that the graph is undirected and has 4 vertices (V = 4) and 5 edges (E = 5). Then, you provided the details of these 5 edges, where each edge is represented by three numbers: the starting vertex, the ending vertex, and the weight of the edge. Here's your input again:

plaintext
Copy code
undirected
4 5
1 2 2
1 3 3
2 3 4
2 4 5
3 4 1
Now, let's go through the provided Python code and see how it processes this input:

graph_type = input(): You enter "undirected," indicating that the graph is undirected.

V, E = map(int, input().split()): You enter "4 5." This means that there are 4 vertices and 5 edges in the graph.

adj_list = [[] for v in range(V)]: An empty adjacency list is created with 4 empty lists because there are 4 vertices.

The loop for i in range(E): iterates 5 times (once for each edge you specified).

In the first iteration, you enter "1 2 2," which means there is an edge from vertex 1 to vertex 2 with a weight of 2. This information is added to adj_list.

In the second iteration, you enter "1 3 3," indicating an edge from vertex 1 to vertex 3 with a weight of 3. This information is also added to adj_list.

The same process continues for the remaining edges.

After processing all the input, the adj_list variable contains the following information about the graph's edges and weights:
'''
#[[(1, 2), (2, 3)], 
# [(0, 2), (2, 4), (3, 5)]
# , [(0, 3), (1, 4), (3, 1)], 
# [(1, 5), (2, 1)]]
'''
Now, let's interpret this adjacency list

The list at index 0 represents vertex 1, and it shows that there are edges from vertex 1 to vertex 2 with a weight of 2 and to vertex 3 with a weight of 3.

The list at index 1 represents vertex 2, and it shows that there are edges from vertex 2 to vertex 1 with a weight of 2, to vertex 3 with a weight of 4, and to vertex 4 with a weight of 5.

Similarly, you can interpret the lists for vertices 3 and 4.

So, the adjacency list stores the relationships between the vertices and the weights of the edges in the graph based on the input you provided.'''