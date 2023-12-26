import sys
import math
input = sys.stdin.readline

def merge_sort(a, p, r):
    if p < r:
        q = (p+r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)

def merge(a, p, q, r):
    global count, result
    i, j = p, q+1
    tmp = []
    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    while i <= q:
        tmp.append(a[i])
        i += 1
    while j <= r:
        tmp.append(a[j])
        j += 1
    i, t = p, 0
    while i <= r:
        a[i] = tmp[t]
        count += 1
        if count == k:
            result = a[i]
            break
        i += 1
        t += 1

n, k = map(int, input().split())
li = list(map(int, input().split()))
count = 0
result = -1
merge_sort(li, 0, n-1)
print(result)