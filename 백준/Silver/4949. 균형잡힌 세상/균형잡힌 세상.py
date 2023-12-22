import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    stack = []
    if string == ".":
        break
    for s in string:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break
    else:
        if not stack:
            print("yes")
        else:
            print("no")
