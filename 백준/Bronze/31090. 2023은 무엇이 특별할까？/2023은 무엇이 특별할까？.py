import sys
input = sys.stdin.readline

def f(n):
    if (n + 1) % int(str(n)[-2:]) == 0:
        return 'Good'
    else:
        return 'Bye'


t = int(input())
for _ in range(t):
    n = int(input())
    print(f(n))