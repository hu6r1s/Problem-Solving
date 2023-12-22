n = int(input())
li = list(map(int, input().split()))
i = 1
stack = []
while li:
    if li[0] == i:
        i += 1
        li.pop(0)
    else:
        stack.append(li.pop(0))

    while stack:
        if stack[-1] == i:
            i += 1
            stack.pop()
        else:
            break
if not stack:
    print("Nice")
else:
    print("Sad")