from collections import defaultdict

def solution(s):
    s = list(map(int, s.replace("{", "").replace("}", "").split(",")))
    d = defaultdict(int)
    for i in s:
        d[i] += 1
    d = dict(sorted(d.items(), key=lambda x: -x[1]))
    return list(d.keys())