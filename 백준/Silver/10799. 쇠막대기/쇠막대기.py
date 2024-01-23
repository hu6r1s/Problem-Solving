string = input()
stack = []
result = 0
for i in range(len(string)):
    if string[i] == "(":
        stack.append(string[i])
    else:
        if string[i-1] == "(":
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
print(result)