moves = [(0,-1),(0,1),(-1,0),(1,0)]
# up , down, left, right

def valid_move (row,column ):
    global steps 
    #checking if it within the matrix bounds and not visited yet
    if  row >= 0 and  row < 10 and column >= 0 and column < 10:
        if steps [row ] [ column ] == 0:
            return True
    return False


# input maze
maze = []
ends = []
# if start and stops are different : use two variable start and stops 
for i in range(10):
    maze.append(input())


# set up the step matrix , 
# 0= not visited yet, any nuymber greater than 0 = its step number , -1 =wall or boundry

steps  = [[0]*10 for r in range(10)]


#iterating throght row and column to identify walls and start , stops . 
for r in range(10):
    for c in range( 10):
        if maze [ r ] [ c ] =="#":
            steps  [ r ][ c ] =  -1 # wall
        if maze [ r ] [ c ] =="X":
            ends.append((r,c))

#  BFS
queue = []
# add the source point to the queue with a distance of 0
queue .append ((ends [0],0))
found = False
min_steps = 0

# BFS BEGINS

while queue != [] and not found:
    #Deque the current position and distance 
    current_pos , distance = queue.pop(0)
    row, column = current_pos

    for dr,dc in moves:
        new_row , new_column = row+dr, column + dc

        #check valide 
        if valid_move(new_row, new_column ):

            #if the destionation is found (not the source) ,set the flag to true
            if maze[new_row][new_column] == "X" and (new_row,new_column) != ends[0]:
                found = True
                min_steps = distance + 1 
                break

            #if not , add new corrdinate to the queue with increased distances
            queue.append(((new_row,new_column),distance +1))
            
            # mark the cell visited by setting it to -1
            steps [new_row][new_column] = -1

print("Minimum steps to reach to destionation 'X'" , min_steps)


'''
Data Storage and Representation:

The code uses two main data structures:
maze: A 2D list representing the layout of the maze. Each cell in the maze can be one of three types: open cell ('.'), wall ('#'), or the source/destination ('X').

steps: Another 2D list of the same dimensions as the maze. It's used to keep track of visited cells and store the minimum number of steps required to reach each cell from the source
. The values in the steps matrix are 0 for unvisited cells, -1 for walls, and positive integers for the minimum steps.



Input:

The input maze is read from the user, and it's assumed to be a 10x10 grid of characters where each character represents a cell in the maze.
The user inputs each row of the maze one by one, and the code appends them to the maze list.
Time Complexity Analysis:
The time complexity of the code can be analyzed in different cases:



Normal Case:
In the normal case, the code performs a BFS traversal of the maze starting from the source point ('X').
The time complexity of BFS is O(V + E), where V is the number of vertices (cells) and E is the number of edges (potential moves).
In the worst case, all cells are visited, so V is at most 100 (for a 10x10 maze), and E is also at most 100 (each cell can have at most four edges).
Therefore, the time complexity in the normal case is O(100 + 100) = O(200), which simplifies to O(1) because it's a constant factor.



Best Case:
In the best case, the destination 'X' is found immediately adjacent to the source 'X' (e.g., the maze is very small).
In this case, BFS may only explore a few cells before finding the destination.
The time complexity would be proportional to the depth of the BFS tree, which can be quite small.
Therefore, the best-case time complexity is O(1) as well.



Worst Case:
In the worst case, the code explores all possible cells before finding the destination.
This would happen if the destination is located as far away from the source as possible in a maze without obstacles.
The worst-case time complexity is O(V + E), as explained in the normal case.
In summary, the time complexity of the code is generally O(1) in practical scenarios due to the small size of the maze. 
However, in the worst case, it can be O(200), which is still considered a constant factor and doesn't depend on the maze's size.'''