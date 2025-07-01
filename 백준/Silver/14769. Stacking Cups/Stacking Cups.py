n = int(input())
li = [input().split() for _ in range(n)]
for l in li:
    if l[0].isdigit():
        l[0], l[1] = l[1], l[0]
        l[1] = int(l[1]) // 2
    else:
        l[1] = int(l[1])
li.sort(key=lambda x: x[1])
for k, _ in li:
    print(k)