'''
        A---------C
        |         |\
        |         | \
        |         |  E
        |         | /
        |         |/
        B---------D
'''

# Adjacency list of the graph

adj_list={
    "A":["B","C"],
    "B":["A","D"],
    "C":["A","D","E"],
    "D":["B","C","E"],
    "E":["C","D"]
}

adj_list={}


class Graph:
    def __init__(self,Nodes,isdirected=False):
        self.nodes=Nodes
        self.adj_list={}
        self.isdirected=isdirected
        for node in self.nodes:
            self.adj_list[node]=[]

    def print_adj_list(self):
        for node in self.nodes:
            print(node, "-->",self.adj_list[node])
    
    def add_edge(self,u,v):
        
        self.adj_list[u].append(v)
        if self.isdirected:
            self.adj_list[v].append(u)
    
    def degree(self,node):
        return len(self.adj_list[node])

        


nodes=["A","B","C","D","E"]
graph=Graph(nodes,isdirected=True)

graph.add_edge("A","B")
graph.print_adj_list()
print(
    graph.degree("A")
)