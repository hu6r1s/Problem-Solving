n = int(input())
stack = []
result = []
num = 1
for _ in range(n):
    x = int(input())
    while num <= x:
        stack.append(num)
        result.append("+")
        num += 1

    if stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        break

if stack:
    print("NO")
else:
    print(*result, sep="\n")