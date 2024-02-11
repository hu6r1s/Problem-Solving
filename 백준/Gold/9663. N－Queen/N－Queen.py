n = int(input())
count = 0
visited1 = [0 for _ in range(n*2)]
visited2 = [0 for _ in range(n*2)]
visited3 = [0 for _ in range(n*2)]

def solve(k):
    global count
    if k == n:
        count += 1
        return

    for i in range(n):
        if visited1[i] or visited2[i+k] or visited3[i-k]:
            continue
        visited1[i] = 1
        visited2[i+k] = 1
        visited3[i-k] = 1
        solve(k+1)
        visited1[i] = 0
        visited2[i+k] = 0
        visited3[i-k] = 0

solve(0)
print(count)