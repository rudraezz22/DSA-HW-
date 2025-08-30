# input two numbers
smallest = int(input("enter your number: "))
largest = int(input("enter your number: "))

# store originals for LCM calculation later
a, b = smallest, largest  

# Euclidean algorithm for HCF
while smallest:
    numstore = smallest
    smallest = largest % smallest
    largest = numstore

hcf = largest
lcm = (a * b) // hcf   # formula: LCM = (a*b)//HCF

print(f"The HCF is {hcf}")
print(f"The LCM is {lcm}")
