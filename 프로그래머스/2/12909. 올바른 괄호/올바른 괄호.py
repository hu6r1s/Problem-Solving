def solution(s):
    s_li = list(s)
    stack = []
    for i in s_li:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True