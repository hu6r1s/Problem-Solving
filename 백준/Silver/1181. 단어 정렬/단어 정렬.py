n = int(input())
li = set()
for _ in range(n):
    string = input()
    li.add(string)


for i in sorted(li, key=lambda i: (len(i), i)):
    print(i)