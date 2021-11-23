def isSorted(stuff):    
    for i in range(1,len(stuff)):
        if stuff[i - 1] > stuff[i]:
           return False
    return True

numbers = [10, 2, 5, 9, 7, 3, 6]

print(isSorted(numbers))
