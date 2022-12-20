"""
Circular Linked List
"""


class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def reader(file):
    file = open(file).readlines()
    return [int(i) for i in file]


def part(file, one = True):
    # lines 18 - 23 are challenge specific
    if not one:
        dkey = 811589153
        rng = 10
    else:
        dkey = 1
        rng = 1

    # initialize index
    idx = []
    # add items into node and multiply them to the cipher key
    for i in file:
        n = dkey * i
        idx.append(Node(n))
    # apply the indexes
    for x, y in zip(idx, idx[1:]):
        x.next = y
        y.prev = x
    # reverse the first and last of the indexed values
    idx[-1].next = idx[0]
    idx[0].prev = idx[-1]

    # Circular viewing
    for i in range(rng):
        # swap values based on their location
        for loc in idx:
            loc.prev.next = loc.next
            loc.next.prev = loc.prev
            x, y = loc.prev, loc.next
            # get the new location
            go_to = loc.val % (len(idx) - 1)
            for _ in range(go_to):
                x = x.next
                y = y.next
            # swap the moved values
            x.next, loc.prev = loc, x
            y.prev, loc.next = loc, y
    # add and return the challenges encryption
    for loc in idx:
        if loc.val == 0:
            a = 0
            tmp = loc
            for l in range(3):
                for k in range(1000):
                    tmp = tmp.next
                a += tmp.val
            print(a)

file = reader('day20.txt')
part(file, one=False)

