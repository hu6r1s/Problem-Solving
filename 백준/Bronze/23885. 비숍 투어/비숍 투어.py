import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())

if n == 1 or m == 1:
    if sx == ex and sy == ey:
        print("YES")
    else:
        print("NO")
elif (ex - sx) % 2 and (ey - sy) % 2:
    print("YES")
elif not (ex - sx) % 2 and not (sy - ey) % 2:
    print("YES")
else:
    print("NO")
#
# 11 12 13
# 21 22 23
# 31 32 33
#
# 짝수,짝수 -> 짝수,짝수
# 홀수,홀수 -> 홀수, 홀수
# 짝수,홀수 -> 짝수,홀수 -> 홀수,짝수
# 홀수,짝수 -> 짝수,홀수 -< 홀수,짝수