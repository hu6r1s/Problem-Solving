t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0
    mx = 0
    for i in range(n-1, -1, -1):
        if mx < arr[i]:
            mx = arr[i]
        else:
            result += mx - arr[i]
    print(result)