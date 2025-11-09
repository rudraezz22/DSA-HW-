n = int(input("enter the number"))

def powercheck(n):
    if n <=0:
      return False
    if n==1:
        return True
    if (n%2) == 0:
        return powercheck(n/2)
    return False
print(powercheck(n))