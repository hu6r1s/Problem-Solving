def solution(players, callings):
    player = dict()
    for idx, value in enumerate(players):
        player[value] = idx
        
    for call in callings:
        curr = player[call]
        player[players[curr-1]] += 1
        player[call] -= 1
        players[curr-1], players[curr] = call, players[curr-1]
        
    return players