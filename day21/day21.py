import re

file = open('puzzle.txt')
file = file.readlines()


working = False

while not working:
    working = True
    for line in file:
        try:
            exec(line)
        except:
            working = False


print(prrg)
print(jntz)