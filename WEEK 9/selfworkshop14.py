

def main():
    
    v,e=map(int,input().split())
    create_adjaceny_matrix(v,e) 
def create_adjaceny_matrix(v,e):
    adjaceny_matrix=[[0]* v for _ in range(e)]
    for i in range(e):
        x,y=map(int,input().split())
        adjaceny_matrix[x][y]=1
        adjaceny_matrix[y][x]=1
    print_adjacency_matrix(adjaceny_matrix)

    

    
def print_adjacency_matrix(adjacency_matrix):
    for i in adjacency_matrix:
        print(" ".join (map(str,i)))
    


if __name__=="__main__":
    main()
