n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
tmp = [0] * n

def solve(k):
    if k == m:
        for i in range(m):
            print(arr[tmp[i]], end=" ")
        print()
        return

    prev = 0

    for i in range(n):
        if prev != arr[i]:
            prev = arr[i]
            tmp[k] = i
            solve(k+1)


solve(0)