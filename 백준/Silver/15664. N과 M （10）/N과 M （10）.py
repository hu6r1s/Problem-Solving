n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
tmp = [0] * n
visited = [0] * n

def solve(k):
    if k == m:
        for i in range(m):
            print(arr[tmp[i]], end=" ")
        print()
        return

    prev = 0
    si = 0
    if k != 0:
        si = tmp[k-1] + 1

    for i in range(si, n):
        if not visited[i] and prev != arr[i]:
            tmp[k] = i
            prev = arr[i]
            visited[i] = 1
            solve(k+1)
            visited[i] = 0


solve(0)