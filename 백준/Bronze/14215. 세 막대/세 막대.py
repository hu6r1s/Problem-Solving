li = list(map(int, input().split()))
li.sort()
print(min(sum(li), (li[0] + li[1]) * 2 - 1))