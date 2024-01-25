string = input()
stack = []
result = 0
chk = 1

for i in range(len(string)):
    if string[i] == "(":
        stack.append(string[i])
        chk *= 2
    elif string[i] == "[":
        stack.append(string[i])
        chk *= 3
    elif string[i] == ")":
        if not stack or stack[-1] != "(":
            result = 0
            break
        if string[i-1] == "(":
            result += chk
        stack.pop()
        chk //= 2
    elif string[i] == "]":
        if not stack or stack[-1] != "[":
            result = 0
            break
        if string[i-1] == "[":
            result += chk
        stack.pop()
        chk //= 3
if not stack:
    print(result)
else:
    print(0)