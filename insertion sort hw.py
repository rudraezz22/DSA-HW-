A = list(map(int, input("Enter elements").split()))


for i in range(1, len(A)):
    value = A[i]
    j = i - 1

    while j >= 0 and value < A[j]:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = value

for r in A:
    print(r)

for i in range(1,len(A)):
     value = A[i]
     j = i - 1
     
     while j>=0 and value<A[j]:
         A[j+1] = A[j]
         j -= 1 
         A[j+1] = value 
         for i in range(len(A)):
             print(A[i])