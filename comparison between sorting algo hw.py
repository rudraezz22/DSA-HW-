def unionOFarrys(A,B,n,m):
    i,j=0,0

    while i<n and j<m:
        if A[i]==B[j]:
            print(A[i],end=" ")
            i+=1
            j+=1

        elif A[i] < B[j]:
            i += 1   # move pointer in A

        else:
            j += 1 

A = [2, 4, 16, 77, 103]
B = [1, 4, 16, 91, 103]

n = len(A)
m = len(B)
unionOFarrys(A,B,n,m)