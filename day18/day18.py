def lava(file):
    output = []
    with open(file) as f:
        reader = f.readlines()
        for line in reader:
            x = tuple(int(i) for i in line.split(','))
            output.append(x)

    return output


def part1(file):
    touching = 0
    cube = [
        (1,0,0),(-1,0,0),(0,1,0),
        (0,-1,0),(0,0,1),(0,0,-1)
        ]
    for x, y, z in file:
        for a,b,c in cube:
            if (x+a,y+b,z+c) not in file:
                touching += 1

    print(touching)


file = lava("part1.txt")