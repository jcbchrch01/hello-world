inputFile = input("Please enter the input file name: ")
outputFile = input("Please enter the output file name: ")

with open(inputFile, 'r') as f, open(outputFile, 'w') as w:
    number = 0
    for line in f:
        number  += 1
        w.write('{:>4}> {}'.format(number, line))
