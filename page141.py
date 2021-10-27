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
>>> example = [1,2]
>>> example
[1, 2]
>>> example.insert(1,10)
>>> example
[1, 10, 2]
>>> example(3,25)

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    example(3,25)
TypeError: 'list' object is not callable
>>> example.insert(3,25)
>>> example
[1, 10, 2, 25]
>>> example = [1,2]
>>> example
[1, 2]
>>> example.append(3)
>>> example
[1, 2, 3]
>>> example extend([11, 12, 13])
SyntaxError: invalid syntax
>>> example.extend([11,12,13])
>>> example
[1, 2, 3, 11, 12, 13]
>>> example + [14,15]
[1, 2, 3, 11, 12, 13, 14, 15]
>>> example
[1, 2, 3, 11, 12, 13]
>>> 
=============================== RESTART: Shell ===============================
>>> example = [1, 2, 10, 11, 12, 13]
>>> example
[1, 2, 10, 11, 12, 13]
>>> example.pop()
13
>>> example
[1, 2, 10, 11, 12]
>>> example.pop(0)
1
>>> example
[2, 10, 11, 12]
>>> 
 RESTART: C:/Users/jrdnc/Documents/Jacob OSUIT/Fall 2021/Script Programming/Assignments/Textbook/Textbook Exercises Week 7/page140pt2.py 
1
>>> 
=============================== RESTART: Shell ===============================
>>> example = [4, 2, 10, 8]
>>> example
[4, 2, 10, 8]
>>> example.sort()
>>> example
[2, 4, 8, 10]
>>> first = [10, 20, 30]
>>> second = first
>>> first
[10, 20, 30]
>>> second
[10, 20, 30]
>>> first[1] = 99
>>> first
[10, 99, 30]
>>> second
[10, 99, 30]
>>> 
