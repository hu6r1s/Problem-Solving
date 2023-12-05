n = int(input())
result = []
for i in range(2, n+1):
    if n % i == 0:
        while n % i == 0:
            n //= i
            result.append(i)
print(*result, sep="\n")