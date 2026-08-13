#no. of islands
def island(grid):
  islands=0
  rows=len(grid)
  col=len(grid[0])

  def dfs(r,c):
    if r<0 or r>=rows or c<0 or c>=col:
      return
    if grid[r][c]=="0":
      return
    grid[r][c]="0"
    dfs(r-1,c) #for up
    dfs(r,c+1) #for right
    dfs(r+1,c) #for bottom
    dfs(r,c-1) #for left

  for r in range(rows):
    for c in range(col):
      if grid[r][c]=="1":
        islands+=1
        dfs(r,c)
  return islands
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(island(grid))