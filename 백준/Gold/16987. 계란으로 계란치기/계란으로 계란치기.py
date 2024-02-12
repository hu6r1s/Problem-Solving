def solve(k):
    global mx, count

    if k == n:
        mx = max(mx, count)
        return

    if arr[k][0] <= 0:
        solve(k+1)
    else:
        flag = False
        for i in range(n):
            if k == i or arr[i][0] <= 0:
                continue
            flag = True
            arr[k][0] -= arr[i][1]
            arr[i][0] -= arr[k][1]
            if arr[k][0] <= 0:
                count += 1
            if arr[i][0] <= 0:
                count += 1
            solve(k+1)
            if arr[k][0] <= 0:
                count -= 1
            if arr[i][0] <= 0:
                count -= 1
            arr[k][0] += arr[i][1]
            arr[i][0] += arr[k][1]
        if not flag:
            solve(k+1)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
count = 0
mx = 0
solve(0)
print(mx)