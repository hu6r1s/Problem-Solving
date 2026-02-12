n = int(input())
p = sorted(list(map(int, input().split())))
s = [0] * n
s[0] = p[0]
for i in range(1, n):
    s[i] = p[i] + s[i-1]

print(sum(s))