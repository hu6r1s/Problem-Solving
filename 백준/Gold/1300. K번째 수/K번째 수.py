import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
start = 1
end = k

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid // i, n)
    if cnt < k:
        start = mid + 1
    else:
        end = mid - 1

print(start)


"""
1 2 3
2 4 6
3 6 9
"""