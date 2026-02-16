import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())

def dfs(v, d):
    if d == n:
        print(v)
        return

    for i in range(1, 10, 2): # 1, 3, 5, 7, 9
        if isPrime(v*10+i):
            dfs(v*10+i, d+1)


def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

dfs(2, 1)
dfs(3, 1)
dfs(5, 1)
dfs(7, 1)