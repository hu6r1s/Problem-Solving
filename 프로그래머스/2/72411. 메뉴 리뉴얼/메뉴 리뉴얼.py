from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    result = []
    orders = [''.join(sorted(o)) for o in orders]
    
    for c in course:
        cnt = defaultdict(int)
        for order in orders:
            for combo in combinations(order, c):
                combo = "".join(combo)
                cnt[combo] += 1
        
        if not cnt:
            continue
        max_cnt = max(cnt.values())
        if max_cnt < 2:
            continue
            
        for com, c in cnt.items():
            if c == max_cnt:
                result.append(com)
                
    return sorted(result)