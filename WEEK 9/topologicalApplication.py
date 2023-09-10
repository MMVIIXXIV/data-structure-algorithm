from topological_sort import *

n, e = map(int, input().split()) # n is number of vertices, e is number of edge
EdgeList = []

for i in range(e):
    x = list(map(int, input().split()))
    EdgeList.append(x)

print(f"EdgeList: {EdgeList}")

vertexList = []
for i in range(len(EdgeList)):
    for j in range(2):
        vertexList.append(EdgeList[i][j])
print(f"VertexList: {vertexList}")

vertexList = list(set(vertexList)) #remove duplicate
vertexList.sort()
print(f"Sorted vertex list: {vertexList}")

vertices = len(vertexList)

ADJList = []
for i in range(len(vertexList)):
    temp = [vertexList[i]]
    for edge in EdgeList:
     
        if edge[0] == vertexList[i]:
            temp.append(edge[1])

    ADJList.append(temp)

result = topological_sort(len(vertexList),ADJList)


print(result)