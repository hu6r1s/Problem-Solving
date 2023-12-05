m = int(input())
n = int(input())
result = []
for num in range(m, n+1):
    count = 0
    if num == 1:
        continue
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        result.append(num)
if result == []:
    print(-1)
else:
    print(sum(result))
    print(min(result))