import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    global result

    visited[x] = 1
    cycle.append(x)
    nx = students[x]
    if visited[nx] == 1:
        if nx in cycle:
            result += cycle[cycle.index(nx):]
            return
    else:
        dfs(nx)

t = int(input())
for _ in range(t):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [1] + [0] * n
    result = []

    for i in range(1, n+1):
        if visited[i] == 0:
            cycle = []
            dfs(i)
    print(n - len(result))