li = [int(input()) for _ in range(10)]
print(sum(li) // len(li))
ans = []
for i in range(len(li)):
    ans.append(li.count(li[i]))
print(li[ans.index(max(ans))])