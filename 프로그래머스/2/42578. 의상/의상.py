from collections import defaultdict

def solution(clothes):
    type = defaultdict(int)
    
    for cloth in clothes:
        type[cloth[1]] += 1
    
    count = 1
    for i in type.values():
        count *= i + 1
    
    return count - 1