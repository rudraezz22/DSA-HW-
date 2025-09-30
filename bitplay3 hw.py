def abcd(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    
    
    max_ones = max(map(len,binary.split('0')))
    return binary, max_ones

print(abcd(5))