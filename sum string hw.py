def sum_string(s):
  def check(a,b,rem):
    if rem=="":
      return True
    total=str(int(a)+int(b))
    if rem.startswith(total):
      return check(b,total,rem[len(total):])
    return False

  n=len(s)
  for i  in range(1,n):
    for j in range(i+1,n):
      first=s[:i]
      second=s[i:j]

      if check(first,second,s[j:]):
        return True

    return False



print(sum_string("112358"))
