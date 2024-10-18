import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
lands = []
for _ in range(n):
    lands += list(map(int, input().split()))

min_time = 500*500*2*257
max_height = 0
sum_land = sum(lands)

for h in range(max(lands), min(lands)-1, -1):
    if sum_land + b >= h * n * m:
        time = 0
        for land in lands:
            diff = land - h
            if diff > 0:
                time += diff * 2
            elif diff < 0:
                time -= diff

        if time < min_time:
            min_time = time
            max_height = h

print(min_time, max_height)