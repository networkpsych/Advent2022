import re


file = open("input.txt")
file = file.read()
x = [i for i in re.findall("\d+", file)]
y = [i for i in re.findall('[A-Z]', file)]
xy = list(zip(x, y))
print(xy)
print(len(xy))
#print(x)
#print(y)