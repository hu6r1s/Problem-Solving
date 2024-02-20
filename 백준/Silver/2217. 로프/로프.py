n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))
s.sort()
result = []
for i in range(n):
    result.append(s[i] * (n - i))
print(max(result))