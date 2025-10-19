def take_input(numbers=None):
    if numbers is None:
        numbers = []
    
    num = int(input("Enter a number (negative to stop): "))
    
    if num < 0:
        return numbers
    
    numbers.append(num)
    return take_input(numbers)


result = take_input()
