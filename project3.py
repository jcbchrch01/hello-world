import math

def newtonSquare(x, estimate = 1):
    if abs(x-estimate ** 2) <= 0.000001:
        return estimate
    else:
        return newtonSquare(x, (estimate + 2 / estimate) / 2)

def main():
    num = int(input('Please enter a positive number: '))
    print (newtonSquare(num,1))

main()
