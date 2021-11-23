def mean(data):
    total = 0
    num_elements =len(data)
    if(num_elements  == 0):
        return(0)
    for item in data:
        total = total + item
    mu = total / (num_elements) # alternately mean = (total / len(data))
    return (mu)

def median(data):
    num_elements =len(data)
    if(num_elements  == 0):
        return(0)
    data.sort()
    # determine even or odd
    even = True
    if len(data)%2 == 1:
        even = False
    if even:
        slice_start = (len(data)//2) - 1
        slice_end   = (len(data)//2) + 1
        me      = sum(data[slice_start:slice_end]) / 2
    else:
        me      = data[len(data)//2]
    return (me)

def mode(data):
    num_elements =len(data)
    if(num_elements  == 0):
        return(0)
    hits = []
    for item in data:
        tally = data.count(item)
        values = (tally, item)
    # Only add one entry for each number in the set
        if values not in hits:
           hits.append(values)
    hits.sort(reverse=True)
    if hits[0][0]>hits[1][0]:
        return(hits[0][1])
    else:
        print("\nThere is not a mode")
        return(0)

if __name__ == "__main__":
    data = [2,4,6,5,7,8]
    print("\nThe mean is:", mean(data))
    print("\nThe median is:", median(data))
    print("\nThe mode is:", mode(data))
