n = int(input())
stack = []
result = []
num = 1
for i in range(n):
    k = int(input())
    while num <= k:
        stack.append(num)
        result.append("+")
        num += 1

    if k <= stack[-1]:
        stack.pop()
        result.append("-")
    else:
        break

if stack:
    print("NO")
else:
    print(*result, sep="\n")



"""
1 2 3 4
1 2
1 2 5 6
1 2 5 7 
7
+ + + + -
"""