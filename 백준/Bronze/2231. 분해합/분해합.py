n = int(input())
li = []
for i in range(1, n+1):
    li_i = list(map(int, str(i)))
    if sum(li_i) + i == n:
        li.append(i)

if len(li) == 0:
    print(0)
else:
    print(min(li))