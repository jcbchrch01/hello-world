def summation(lower, upper, margin):
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + summation(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result
