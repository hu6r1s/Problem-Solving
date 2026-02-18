import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())

friend = [[] for _ in range(n)]
visited = [False] * n
flag = False

for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)


def dfs(v, d):
    global flag

    if d == 5:
        flag = True
        return

    visited[v] = True
    for i in friend[v]:
        if not visited[i]:
            dfs(i, d + 1)
    visited[v] = False


for i in range(n):
    dfs(i, 1)
    if flag:
        print(1)
        break
else:
    print(0)