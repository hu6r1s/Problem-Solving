n = int(input())
m = int(input())
lst = list(map(int, input().split()))
lst.sort()

s, e = 0, n-1
cnt = 0

while s < e:
    if lst[s] + lst[e] == m:
        cnt += 1
        s += 1
        e -= 1
    elif lst[s] + lst[e] < m:
        s += 1
    else:
        e -= 1
print(cnt)


"""
1 2 3 4 5 7
"""