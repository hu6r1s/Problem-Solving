from collections import defaultdict

def solution(N, stages):
    d = defaultdict(int)
    cnt = len(stages)
    for i in range(1, N+1):        
        if not cnt:
            d[i] = 0
        else:
            d[i] = stages.count(i) / cnt
            cnt -= stages.count(i)
    return list(sorted(d, key=lambda x: (-d[x], x)))