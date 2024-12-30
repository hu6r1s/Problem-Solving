from collections import defaultdict

def solution(participant, completion):
    lst = defaultdict(int)
    
    for part in participant:
        lst[part] += 1
    
    for com in completion:
        lst[com] -= 1
    
    for name in lst:
        if lst[name]:
            return name