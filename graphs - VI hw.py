def dfs(graph,start,visited):
    

    
    visited.add(start)
    
    for neighbour in graph[start]:
       if neighbour not in visited:
          
          dfs(graph,neighbour,visited)

g = {
   0:[1],
   1:[2],
   2:[3],
   3:[],
   4:[5],
   5:[]

}
visited = set()
dfs(g,0,visited=visited)
print(f"nodes not reachable from A ")
for i in range(6):
   if i not in visited:
      print(i)
