def abcd(lst):
    if lst == []:
        return 0
    else:
          return 1 + abcd(lst[1:])

lst = [65,95,2,97,83]
print(abcd(lst))