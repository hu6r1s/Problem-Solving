n, k = map(int, input().split())
li = []
for i in range(1, n+1):
    if n % i == 0:
        li.append(i)
if k <= len(li):
    print(li[k-1])
else:
    print(0)