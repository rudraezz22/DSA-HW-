def abcd(n):
    decimal = 0
    power = 0

    while n>0:
        digit = n%10
        if digit ==1:
            decimal += 2**power
        power +=1
        n//=10
    return decimal
print(abcd(1011))