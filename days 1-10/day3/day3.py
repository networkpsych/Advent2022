import string
from collections import Counter


LETTERS = {val:key for key, val in enumerate(string.ascii_letters)}
# UPPER = {val:key+1 for key, val in enumerate(string.ascii_lowercase)}

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

def partOne():
    with open('items.txt') as ruck:

        boundary = 0
        badge = set()
        ruck_sack = ruck.readlines()
        for line in ruck_sack:
            idx = len(line)//2
            a, b = line[0:idx], line[idx:len(line)]
            badge.add(rucksack(a, b))
            boundary += LETTERS[badge.pop()]+1
    print(boundary)


def part2():
    with open('items.txt') as ruck:
        boundary = 0
        ruck_sack = ruck.readlines()
        for sack in range(0,len(ruck_sack),3):
            a, b, c = ruck_sack[sack:sack+3]
            items = (set(a.strip()) & set(b.strip()) & set(c.strip())).pop()
            boundary += LETTERS[items] + 1
        print(boundary)
                
                

partOne()
part2()