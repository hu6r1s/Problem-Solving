n = int(input())
height = [0] + list(map(int, input().split()))
stack = [(100000001, 0)]
result = []
for i in range(1, n+1):
    while height[i] > stack[-1][0]:
        stack.pop()
    result.append(stack[-1][1])
    stack.append((height[i], i))

print(*result, sep=" ")