result = 0

for _ in range(5):
    n = int(input())

    if n <= 40:
        result += 40
    else:
        result += n

print(result//5)