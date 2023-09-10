
'''
maze:  the input maze
ends:  the list of source and destination coordinates
steps: matrix that stores the minimum number of steps from
       the source coordinate to each visited maze cell.
       = -1 if the cell is part of a wall.
'''





# relative distance of above, below, left, and right cells
adj = [(0,-1),(0,1),(-1,0),(1,0)]

def valid(r,c):
    # return True if coordinate (r,c) is not outside the matrix
    # and is not a part of a wall
    
    global steps
    
    if r >= 0 and r < 10 and c >= 0 and c < 10:
        if steps[r][c] == 0:# Check if the cell is not visited yet (steps[r][c] = 0)
            return True
    return False


# Read input maze
maze = []
ends = []
for r in range(10):
    maze.append(input())



# Set up the steps matrix
steps = [[0]*10 for r in range(10)] #set all as 0 at first
for r in range(10):
    for c in range(10):
        if maze[r][c] == '#':
            steps[r][c] = -1        # Mark walls as -1
        if maze[r][c] == 'X':
            ends.append((r,c))      # ends Remember the source and destination


# Breadth-First Search       
queue = []


# Add the source point to the queue with a distance of 0
queue.append((ends[0], 0))

found=False
min_steps=0
while queue != [] and not found:
    current_pos, distance = queue.pop(0)
    row, column= current_pos

    for dr,dc in adj:
        new_row,new_column=row+dr,column+dc

        if valid(new_row,new_column):
            if maze[new_row][new_column] == 'X' and (new_row, new_column) != ends[0]:
                found=True
                min_steps =distance+1  
                break  
            queue.append(((new_row,new_column),distance+1))
            steps[new_row][new_column]=-1   #marking cells as visited


# Print the minimum steps to reach the destination 'X'
print("Minimum steps to reach the destination 'X':", min_steps)


                


        

