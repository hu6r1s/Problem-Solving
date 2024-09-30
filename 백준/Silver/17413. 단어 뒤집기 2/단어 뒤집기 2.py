from collections import deque

str_lst = input()
stack = deque([])
rst_str = ""
tag = False

for s in str_lst:
    if s == " ":
        stack.append(" ")
        rst_str += "".join(stack)
        stack.clear()
    elif s == "<":
        stack.append(s)
        tag = True
    elif s == ">":
        stack.append(s)
        tag = False
        rst_str += "".join(stack)
        stack.clear()
    else:
        if tag:
            stack.append(s)
        else:
            stack.appendleft(s)

rst_str += "".join(stack)

print(rst_str)