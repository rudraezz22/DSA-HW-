n = 3
e = 3

edges = [(0,1),(1,2),(2,0)]
l1 = []
for i in range(n):
    l1.append([])

for edge in edges:
    x  = edge[0]
    y = edge[1]

    l1[x].append(y)
    l1[y].append(x)

for i in range(n):
    print(i,"->",l1[i])