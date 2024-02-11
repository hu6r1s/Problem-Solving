n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0] * n
tmp = [0] * n

def solve(k):
    if k == m:
        for i in range(m):
            print(arr[tmp[i]], end=" ")
        print()
        return

    for i in range(n):
        if not visited[i]:
            tmp[k] = i
            visited[i] = 1
            solve(k+1)
            visited[i] = 0


solve(0)