import sys
input = sys.stdin.readline

s = int(input())
start = 1
end = 4294967295
result = 0

while start <= end:
    mid = (start + end) // 2
    if mid * (mid + 1) / 2 <= s:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)