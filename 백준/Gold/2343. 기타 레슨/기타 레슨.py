import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
start = max(a) # 레슨의 최댓값
end = sum(a) # 레슨의 총합

while start <= end:
    mid = (start + end) // 2
    sum = 0
    cnt = 0
    for i in range(n):
        if sum + a[i] > mid:
            cnt += 1
            sum = 0
        sum += a[i]
    if sum != 0:
        cnt += 1
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)