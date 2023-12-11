n = int(input())
li = list(map(int, input().split()))
sorted_li = sorted(set(li))
result = dict()
for i in range(len(sorted_li)):
    result[sorted_li[i]] = i
for i in li:
    print(result[i], end=" ")