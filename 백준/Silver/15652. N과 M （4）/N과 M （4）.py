n, m = map(int, input().split())
arr = [0] * n

def solve(k):
    if k == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return

    si = 1
    if k != 0:
        si = arr[k-1]

    for i in range(si, n+1):
        arr[k] = i
        solve(k+1)


solve(0)