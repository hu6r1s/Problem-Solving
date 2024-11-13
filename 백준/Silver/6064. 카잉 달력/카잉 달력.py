import math


t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    max_year = math.lcm(m, n)
    answer = x
    while answer <= max_year:
        if (answer - 1) % n + 1 == y:
            break
        answer += m
    if answer > max_year:
        print(-1)
    else:
        print(answer)