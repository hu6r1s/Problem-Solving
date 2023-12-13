n, m = map(int, input().split())
li = dict()
count = 0
result = []
for _ in range(n):
    li[input()] = True
for _ in range(m):
    s = input()
    if s in li.keys():
        count += 1
        result.append(s)
result.sort()
print(count)
print(*result, sep="\n")