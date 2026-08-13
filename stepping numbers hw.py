n=10
m=16
for i in range(n,m+1):
    s=str(i)
    if abs(int(s[0])-int(s[1]))==1:
        print(i)
    else:
        pass