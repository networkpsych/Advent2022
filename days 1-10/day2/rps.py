"""
Pt 1

A = Rock (1 point)
B = Paper (2 point)
C = Scissors (3 point)

Y = Win (6 point)
X = Loss (0 point)
Z = Tie (3 point)

Win = choice + 6
Tie = choice + choice
Loss = choice + 0
"""

def score(item):
    out = {
        "A Y": 7, "B Y": 8, "C Y": 6,
        "A Z": 3, "B Z": 4, "C Z": 5,
        "A X": 2, "B X": 0, "C X": 1,
    }

    return out[item] + 1


file = open("D:/advent2022/day2/rps.txt")
file = file.read().split('\n')[:-1]
#file = [["A Y"], ["B X"],["C Z"]]
x = []
for line in file:
    x.append(score(line))

print(sum(x))
