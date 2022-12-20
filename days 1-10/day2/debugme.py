rpsValue = {'A':1, 'B':2, 'C': 3} # Rock Paper Scissors values
rpsWC = {'A': 'C', 'B': 'A', 'C':'B' } # Win condition
rpsLC = {val: key for (key, val) in rpsWC.items()} # Lose condition

def roundOutcome(game):
    wdlValue = [6,3,0]
    if rpsWC[game[0]] == game[1]:
        return wdlValue[2]
    elif rpsWC[game[1]] == game[0]:
        return  wdlValue[0]
    else:
        return wdlValue[1]

def play_round_strategy_1(game):
    equivalences = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    t_game = [game[0],equivalences[game[1]]]
    return roundOutcome(t_game) + rpsValue[t_game[1]] 


def play_round_strategy_2(game):
    if game[1] == 'X':
        selected = rpsWC[game[0]]
    elif game[1] == 'Z':
        selected = rpsLC[game[0]]
    else:
        selected = game[0]

    return rpsValue[selected] + roundOutcome([game[0],selected])

with open("./day2/rps.txt") as f:
    L = [x.split(" ") for x in f.read().split("\n")[:-1]]
    res1 = sum(map( play_round_strategy_1,L))
    print(f"first strategy: {res1}")