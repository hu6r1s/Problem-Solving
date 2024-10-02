from collections import defaultdict

n = int(input())
d = defaultdict(int)
d['Q1'] = d['Q2'] = d['Q3'] = d['Q4'] = d['AXIS'] = 0
for _ in range(n):
    x, y = map(int, input().split())

    if x > 0 and y > 0:
        d['Q1'] += 1
    elif x < 0 and y > 0:
        d['Q2'] += 1
    elif x < 0 and y < 0:
        d['Q3'] += 1
    elif x > 0 and y < 0:
        d['Q4'] += 1
    else:
        d['AXIS'] += 1

for k, v in d.items():
    print("{}: {}".format(k, v))