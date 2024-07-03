n = int(input())
li = [input() for _ in range(n)]
s = dict()
for i in set(li):
    s[i] = li.count(i)
result = []
for key, value in s.items():
    if s[key] == max(s.values()):
        result.append(key)

result.sort()
print(result[0])