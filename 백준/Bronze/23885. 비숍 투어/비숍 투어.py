import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())

if sx % 2 and sy % 2:
    if ex % 2 and ey % 2:
        print("YES")
    else:
        print("NO")
elif not sx % 2 and not sy % 2:
    if not ex % 2 and not ey % 2:
        print("YES")
    else:
        print("NO")
elif not sx % 2 or not sy % 2:
    if not ex % 2 or not ey % 2:
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