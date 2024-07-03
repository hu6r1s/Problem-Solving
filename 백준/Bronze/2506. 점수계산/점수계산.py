score = 0
result = 0
n = int(input())
slv = list(map(int, input().split()))
for s in slv:
    if not s:
        score = 0
    else:
         score += 1
    result += score
print(result)