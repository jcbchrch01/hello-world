def displayRange(lower, upper):
    if lower <= upper:
        print(lower)
        displayRange(lower + 1, upper)
        
