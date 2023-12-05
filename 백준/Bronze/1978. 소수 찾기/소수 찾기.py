n = int(input())
li = list(map(int, input().split()))
if 1 in li:
    li.remove(1)
result = 0
for l in li:
    count = []
    for i in range(1, l+1):
        if l % i == 0:
            count.append(i)
    if len(count) == 2:
        result += 1
print(result)