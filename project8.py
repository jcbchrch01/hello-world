def printAll(seq):
    if seq:
        print(seq[0])
        printAll(seq[1:])
printAll("This is for project 8 on page 204.")
printAll((1,2,3,4))
printAll([1,2,3,4])
