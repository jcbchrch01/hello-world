def summation(lower, upper):
    if lower > upper:
        return 0
    else:
        return reduce(lambda x, y: x+y,
                      range(lower, upper + 1))
