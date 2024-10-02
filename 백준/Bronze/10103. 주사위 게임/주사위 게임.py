n = int(input())
c_point = s_point = 100

for _ in range(n):
    c, s = map(int, input().split())

    if c > s:
        s_point -= c
    elif c < s:
        c_point -= s

print(c_point, s_point, sep='\n')