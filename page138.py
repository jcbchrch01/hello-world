Python 2.7.17 (v2.7.17:c2f86d86e6, Oct 19 2019, 21:01:17) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> x = 2
>>> [x, math.sqrt(x)]
[2, 1.4142135623730951]
>>> [x + 1]
[3]
>>> first = [1, 2, 3, 4]
>>> second = list(range(1, 5))
>>> first
[1, 2, 3, 4]
>>> second
[1, 2, 3, 4]
>>> third = list("Hi there!")
>>> third
['H', 'i', ' ', 't', 'h', 'e', 'r', 'e', '!']
>>> len(first)
4
>>> first[0]
1
>>> first[2:4]
[3, 4]
>>> first + [5, 6]
[1, 2, 3, 4, 5, 6]
>>> first == second
True
>>> 
=============================== RESTART: Shell ===============================
>>> print("1234")
1234
>>> print([1, 2, 3, 4])
[1, 2, 3, 4]
>>> 3 in [1,2 ,3]
True
>>> 0 in [1, 2, 3]
False
>>> 
=============================== RESTART: Shell ===============================
>>> example [1, 2, 3, 4]

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    example [1, 2, 3, 4]
NameError: name 'example' is not defined
>>> example = [1, 2, 3, 4]
>>> example
[1, 2, 3, 4]
>>> example[3] = 0
>>> example
[1, 2, 3, 0]
>>> numbers = [2, 3, 4, 5]
>>> numbers
[2, 3, 4, 5]
>>> for index in range(lens(numbers)):
	numbers[index] = numbers[index] ** 2

	

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    for index in range(lens(numbers)):
NameError: name 'lens' is not defined
>>> for index in range(len(numbers)):
	numbers[index] = numbers[index] ** 2

	
>>> numbers
[4, 9, 16, 25]
>>> sentence = "This example has five words
SyntaxError: EOL while scanning string literal
>>> sentence = "THIS EXAMPLE HAS FIVE WORDS"
>>> words = sentence.split()
>>> words
['THIS', 'EXAMPLE', 'HAS', 'FIVE', 'WORDS']
>>> for index in range(len(words)):
	words[index] = words[index].upper()

	
>>> words
['THIS', 'EXAMPLE', 'HAS', 'FIVE', 'WORDS']
>>> 
