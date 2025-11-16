notes = [500,100,50,10]
target = 2030

def find_combinations(i,amount,current):
    if amount == 0:
        print(current)
        return
    if i == len(notes) or amount<0:
        return
    
    note = notes[i]
    max_count = amount//note

    for count in range(max_count+1):
        find_combinations(i+1,amount-count*note,current+[(note,count)])
find_combinations(0,target,[])