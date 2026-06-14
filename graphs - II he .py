import heapq

def func(n):
    heap = []
    heapq.heappush(heap,(0,1))

    for i in range(n):
        a,b = heapq.heappop(heap)
        print(a,end=" ")

        heapq.heappush(heap,(b,a+b))
        

func(5)

