import functools

file = open("project9integers.txt", 'r')
file = file.read()
file = file.split()
file = list(map(int, file))

print(functools.reduce(lambda x, y: x + y / len(file), file, 0))
