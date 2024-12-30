from collections import defaultdict

def solution(genres, plays):
    sing = defaultdict(list)
    play = defaultdict(int)
    for i in range(len(genres)):
        sing[genres[i]].append([i, plays[i]])
        play[genres[i]] += plays[i]
    
    play = sorted(play, key=lambda x: play[x], reverse=True)
    for key in sing:
        sing[key].sort(key=lambda x: (-x[1], x[0]))
    
    result = []
    for i in play:
        tmp = [value[0] for value in sing[i][:2]]
        result += tmp

    return result