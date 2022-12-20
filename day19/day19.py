import re


def get_file(file):
    file = open(file).readlines()
    return [f.strip() for f in file]

def qual_h(state):
    """
    Returns the quality of current branch
    Quality:
        if it is over 10,000, send it.
    """
    minutes, (robots, inventory, mined) = state
    return 1000*mined[3] + 100*mined[2] + 10*mined[1] + mined[0]

def bfs(r, cost, min_t, max_queue):
    queue = []
    # add time, robot, r_inventory, r_mined
    queue.append((0,(r, (0,0,0,0), (0,0,0,0))))
    geo_mined = 0
    depth = 0 # depth of tree
    while queue:
        m, (r, old_inv, mined) = queue.pop(0) # get current queue

        if m > depth:
            queue.sort(key=qual_h, reverse=True)
            queue = queue[:max_queue]
            depth = m
        
        if m == min_t:
            geo_mined = max(geo_mined, mined[3])
            continue

        # add ore
        new_inv = tuple([old_inv[i] + r[i] for i in range(4)])
        new_mined = tuple([mined[i] + r[i] for i in range(4)])

        # if not building
        queue.append(m+1, (r, new_inv, new_mined))

        # build new robots
        for i in range(4):
            cost_r = cost[i]

            if all([old_inv[j] >= cost_r[j] for j in range(4)]):
                new_r = list(r)
                new_r[i] += 1
                new_r = tuple(new_r)

                # new state
                new_i_st = tuple([new_inv[j] - cost_r[j] for j in range(4)])
                queue.append((m+1, (new_r, new_i_st, new_mined)))
    return geo_mined


file = get_file('sample.txt')
items = []

for f in file:
    items.append([int(i) for i in re.findall(r'\d+', f)])

max_time = 24
sum_qual = 0
print(items)


for id, ore_o, clay_c, obs_o, obs_c, geo_o, geo_c in items:
    robot_costs = [
        (ore_o, 0,0,0),
        (clay_c, 0,0,0),
        (obs_o, obs_c, 0,0),
        (geo_o, 0, geo_c,0)
    ]

    mined = bfs(robot_costs, (1,0,0,0), max_time, max_queue=100)

    sum_qual += mined*id
    print(f"Blueprint {id}: geodes - {mined}")
print(f"Quality: {sum_qual}")