def abcd(a):
  n = len(a)
  powersetsize = 2**n
  for outer in range(powersetsize):
    subset = ""
    for inner in range(n):
      if outer & (inner<<1):
        subset += a[inner]
    print(subset)

input1 = input("enter your string")
abcd(input1)