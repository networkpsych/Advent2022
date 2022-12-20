import itertools
import csv

def parser(val):
    valves = {}
    flow = {}
    with open(val, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if "Valves" in row:
                continue
            else:
                valves[row[0]] = row[2:]
                flow[row[0]] = row[1]
    return valves, flow

graph, flow = parser('sample.csv')


visited = [] # List for visited nodes.
queue = []   #Initialize a queue
total = []

def bfs(visited, graph, node, flow): #function for BFS
    visited.append(node)
    queue.append(node)
    i = 30
    max_flow = max([int(i) for i in flow.values()])
    visited_flow = []
    total = max_flow
    full_items = graph.keys()
    j = 0
    while queue:          # Creating loop to visit each node
        m = queue.pop() 
        print (m, end = " ") 

        for n in graph[m]:
            tmp = int(flow[n])
            if n not in visited:
                visited.append(n)
                queue.append(n)
                if tmp > 0 and n not in visited_flow:
                    visited_flow.append(n)
                    total += tmp
                else:
                    total += total
            if n in visited_flow:
                total += total
                
        i-=1
        if i == 0:
            j+=1
            i = 30
            total = 0
            if j == 10:
                break
            bfs(visited, graph, full_items[j])
        if total == 1651:
            break
            
    print(total)
        

# Driver Code
bfs(visited, graph, 'AA', flow)    # function calling
