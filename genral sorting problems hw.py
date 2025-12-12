def rotations(a,n,a_size):
    for i in range(n):
        rotate(a,a_size)
def rotate(a,a_size):
    temp = a[0]
    for i in range(a_size-1):
        a[i] = a[i+1]
    a[a_size-1] = temp
def print1(a,a_size):
    print(a,end=" ")

a = list(map(int,input("enter elements eperated by space").split()))
rotations(a,2,len(a))
print1(a,len(a))