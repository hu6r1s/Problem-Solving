n = int(input())
li = []
for _ in range(n):
    x, y = input().split()
    li.append((x, y))
li.sort(key=lambda i: (int(i[0])))
for x, y in li:
    print(x, y)