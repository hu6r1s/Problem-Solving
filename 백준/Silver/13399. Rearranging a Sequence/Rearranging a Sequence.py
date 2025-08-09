import sys
input = sys.stdin.readline

n, m = map(int, input().split())
request = [int(input()) for _ in range(m)]
seen = set()
result = []

for req in reversed(request):
    if not req in seen:
        seen.add(req)
        result.append(req)

for i in range(1, n+1):
    if i not in seen:
        result.append(i)

print(*result, sep='\n')