def solution(s):
    stack = []
    for string in s:
        if string == "(":
            stack.append(string)
        else:
            if not stack:
                return False
            stack.pop()
    else:
        if stack:
            return False
        else:
            return True