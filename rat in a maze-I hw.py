n=4

def check(maze,x,y,res):
    if 0<=x<n and 0<=y<n:
        if maze[x][y]==1 and res[x][y]==0:
            return True
    return False

def ratMaze(maze,x,y,res):
    
    if x==n-1 and y==n-1:
        return 1

    moves=[(-1,0),(1,0),(0,-1),(0,1)]
    count=0
    for dx,dy in moves:
        new_x=x+dx
        new_y=y+dy

        if check(maze,new_x,new_y,res):
            res[new_x][new_y]=1
            count+=ratMaze(maze,new_x,new_y,res)
            
            res[new_x][new_y]=0
    return count

def SolveMaze(maze):
    res = [[0]*n for _ in range(n)]
    res[0][0]=1

    count = ratMaze(maze, 0, 0, res)

    return count

maze=[[1,0,0,0],
      [1,1,1,0],
      [0,1,1,0],
      [0,1,1,1]
      


      ]
print(SolveMaze(maze))
