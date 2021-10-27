>>> for number in [6, 4 , 8]:
        print(number, end = " ")

6 4 8
>>> for character in "Hi there!":
        print(character, end = " ")

H i   t h e r e !
>>> list(range(1, 6, 1))
[1, 2, 3, 4, 5]
>>> list(range(1, 6, 2))
[1, 3, 5]
>>> list(range(1, 6, 3))
[1, 4]
>>> theSum = 0
>>> for count in range(2, 11, 2)):
        theSum += count
>>> theSum
30

>>> for count in range(10, 0, -1):
        print(count, end = " ")
10 9 8 7 6 5 4 3 2 1
>>> list(range(10, 0, -1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
