def red_input():
    n= int(input())
    graph =[[] for _ in range( n+1)]
    
    for u in range( 1, n+1):
        data = list (map(int,input().split()))