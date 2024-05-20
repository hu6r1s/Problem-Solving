def solution(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
            continue
            
        stack.append(i)
    if stack:
        return 0
    else:
        return 1