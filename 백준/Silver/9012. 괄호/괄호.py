import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().strip()
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")