n = int(input())
init = 2
for i in range(n):
    init += 2 ** i
print(init ** 2)