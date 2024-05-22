string = input()
bomb = input()
stack = []
for s in string:
    stack.append(s)
    if stack[-1] == bomb[-1] and "".join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

if stack:
    print(*stack, sep="")
else:
    print("FRULA")