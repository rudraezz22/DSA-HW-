def jobSequence(arr,t):
    n= len(arr)

    for i in range(n):
        for j in range(n-1-i):
            if arr[j][2]<arr[j+1][2]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    result=[False]*t

    job=["-1"]*t

    for i in range(n):
        for j in range(min(t-1,arr[i][1]-1),-1,-1):
            if result[j] is False:
                result[j]=True
                job[j]=arr[i][0]
                break
    print(job)
    total_loss = 0

    for i in range(n):
        if arr[i][0] not in job:
            total_loss += arr[i][2]

    print("Job sequence:", job)
    print("Minimum loss:", total_loss)

arr=[
    ["a",2,100],
    ["b",1,19],
    ["c",2,27],
    ["d",1,25],
    ["e",3,15]
]

jobSequence(arr,3)