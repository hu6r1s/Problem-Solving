n, m = map(int, input().split())
arr = [0] * n

def solve(k):
    if k == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return


    for i in range(1, n+1):
        arr[k] = i
        solve(k+1)


solve(0)