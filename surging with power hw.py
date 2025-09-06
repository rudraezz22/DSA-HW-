n = int(input("Enter your number: "))

if n & (n - 1) == 0:
    if n == 1:
        print("It is a power of 8 (8^0)")
    elif n % 10 in (2, 4, 6, 8):
        print("It is a power of 8")
    else:
        print("It is not a power of 8")
else:
    print("It is not a power of 8")
