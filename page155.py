Python 2.7.17 (v2.7.17:c2f86d86e6, Oct 19 2019, 21:01:17) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits = ("apple", "banana")
>>> fruits
('apple', 'banana')
>>> meats = ("fish", "poultry")
>>> meats
('fish', 'poultry')
>>> food = meats + fruits
>>> food
('fish', 'poultry', 'apple', 'banana')
>>> veggies = ["celery", "beans"]
>>> tuple(veggies)
('celery', 'beans')
>>> badSingleton = (3)
>>> badSingleton
3
>>> goodSingleton = (3,)
>>> goodSingleton
(3,)
>>> 
 RESTART: C:/Users/jrdnc/Documents/OSU-IT Jordan/OSU-IT/Fall 2020/Script Programming/ITD2313-Portfolio-ChurchJordan/Assignments/Hands-on _ Labs/Textbook Exercises - Week 7/146.py 
>>> 
 RESTART: C:/Users/jrdnc/Documents/Jacob OSUIT/Fall 2021/Script Programming/Assignments/Textbook/Textbook Exercises Week 7/page147.py 
>>> average([1, 3, 5 ,7])
0
>>> 
=============================== RESTART: Shell ===============================
>>> info = {}
>>> info["name"] = "Sandy"
>>> info["occupation"] = "hacker"
>>> info
{'name': 'Sandy', 'occupation': 'hacker'}
>>> info["occupation"] = "manager"
>>> info
{'name': 'Sandy', 'occupation': 'manager'}
>>> info["name"]
'Sandy'
>>> info["job"]

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    info["job"]
KeyError: 'job'
>>> info["occupation"]
'manager'
>>> if "job" in info:
	print(info.["job"])
	
SyntaxError: invalid syntax
>>> print(info.get("job", None))
None
>>> print(info.pop("job", None))
None
>>> print(info.pop("occupation"))
manager
>>> info
{'name': 'Sandy'}
>>> for key in info:
	print(key, info[key])

	
('name', 'Sandy')
>>> grades = {90:'A', 80:'B', 70:'C'}
>>> list(grade.items())

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    list(grade.items())
NameError: name 'grade' is not defined
>>> list(grades.items())
[(80, 'B'), (90, 'A'), (70, 'C')]
>>> for (key, value) in grades.items():
	print(key, value)

	
(80, 'B')
(90, 'A')
(70, 'C')
>>> 
