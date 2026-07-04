#m coloring problem
def is_safe(node,color,colors,graph):
  for neighbour in range(len(graph)):
    if graph[node][neighbour]==1 and colors[neighbour]==color:
      return False
  return True


def mcoloring(node,m,colors,graph):
  if node ==len(graph):
    return True
  for color in range(1,m+1):
      if is_safe(node,color,colors,graph):
        colors[node]=color
      
        if mcoloring(node+1,m,colors,graph):
          return True
      
        colors[node]=0
  return False


graph = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
]

m = 3

colors = [0] * len(graph)

if mcoloring(0, m, colors, graph):
    
    print(colors)
else:
    print("No Solution Exists")