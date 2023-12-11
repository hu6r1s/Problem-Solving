n = int(input())
li = []
for _ in range(n):
    x, y = map(int, input().split())
    li.append((x, y))
li.sort(key=lambda i: (i[1], i[0]))
for x, y in li:
    print(x, y)