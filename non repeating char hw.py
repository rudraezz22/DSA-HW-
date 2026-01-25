target = "aabbcdd"
dict1 = {}
for i in target:
  if i in dict1:
    dict1[i]+=1
  else:
    dict1[i]=1
for j in dict1:
  if dict1[j] == 1:
    print(j)
