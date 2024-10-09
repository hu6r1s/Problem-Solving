import math 

n = int(input())
lst = list(map(int, input().split()))
t, p = map(int, input().split())

t_cnt = 0
for l in lst:
    if l:
        t_cnt += math.ceil(l / t)

print(t_cnt)
print(n//p, n % p)