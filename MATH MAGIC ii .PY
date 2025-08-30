
n = int(input("enter ur number"))
if n>1:
    for i in range(2,n):
        if n % i ==0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")
else:
    print("its not a prime number")

#prime numbers only:

l = int(input("enter lower num"))
h = int(input("enter higher num"))
store = []
for j in range(l,h+1):
    for i in range(2,j):
        if j%i==0:
            
            break
    else:
        store.append(j)
        

print(store)

#seive of erethoseness (group of prime numbers) : O(logn)
def seive(num):
    l1 = [True for i in range(num+1)]
    p = 2

    while p*p<=num:
      if l1[p]==True:
          for x in range(p*p,num+1,p):
              l1[x]=False
      p +=1

    for i in range(2,num+1):
        if l1[i]:
            print(i)
       
seive(56)