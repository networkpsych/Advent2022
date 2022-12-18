import string
from collections import Counter


def rucksack(a, b):
    letters = ''
    for i in a:
        for j in b:
            if i == j:
                letters = i
                break
        if i == j:
            break
        
    return letters



lower_letters = {}
upper_letters = {}

for key, val in enumerate(string.ascii_lowercase):
    lower_letters[val] = key+1

for key, val in enumerate(string.ascii_uppercase):
    lower_letters[val] = key+27

ruck_sack = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

i = 0

with open('items.txt') as ruck:
    boundary = 0
    badge = set()
    ruck_sack = ruck.readlines()
    for line in ruck_sack:
        idx = len(line)//2
        a, b = line[0:idx], line[idx:len(line)]
        badge.add(rucksack(a, b))
        print(badge)
        if boundary % 3 == 0 and len(badge) == 1:
            tmp = list(badge)[0]
            if tmp in lower_letters.keys():
                i += lower_letters[tmp]
            elif badge in upper_letters.keys():
                i += upper_letters[tmp]
            badge.pop()
        elif len(badge) > 1 and boundary % 3 == 0:
            print(badge)
            break

    
print(i)