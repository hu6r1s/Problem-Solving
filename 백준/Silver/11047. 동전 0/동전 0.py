n, k = map(int, input().split())
d = []
for _ in range(n):
    d.append(int(input()))

d.sort(reverse=True)
count = 0

for i in d:
    count += k // i
    k %= i
print(count)