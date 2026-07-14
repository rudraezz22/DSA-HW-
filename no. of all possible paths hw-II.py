def dfs(graph,start,dest,visited):
    if start==dest:
        return 1
    print(start,"->",end=" ")
    visited.add(start)
    count=0
    for neighbour in graph[start]:
        if neighbour not in visited:
            count+=dfs(graph,neighbour,dest,visited)
    visited.remove(start)
    print("\n")
    
    return count

graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

total_paths = dfs(graph, 0, 2, visited=set())
print(f"\nthe no. of paths are: {total_paths}")