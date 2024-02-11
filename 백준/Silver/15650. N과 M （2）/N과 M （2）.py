n, m = map(int, input().split())
arr = [0] * n
visited = [0] * (n+1)

def solve(k):
    if k == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return

    si = 1
    if (k != 0):
        si = arr[k-1] + 1

    for i in range(si, n+1):
        if not visited[i]:
            arr[k] = i
            visited[i] = 1
            solve(k+1)
            visited[i] = 0


solve(0)