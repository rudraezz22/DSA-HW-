y = [[8, 4, 1],
     [5, 6, 3],
     [77, 21, 32]]

ans = 0
for i in range(len(y)):
    for j in range(len(y[0])):
        ans = ans + y[i][j]   # row-wise addition
    print(ans, end=" ")
    ans = 0
