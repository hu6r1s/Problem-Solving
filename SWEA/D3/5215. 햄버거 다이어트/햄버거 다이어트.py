def dfs(v, score, cal):
    global total_score

    if cal > L:
        return

    if score > total_score:
        total_score = score

    if v == n:
        return

    s, c = li[v]
    dfs(v + 1, score + s, cal + c)
    dfs(v + 1, score, cal)


T = int(input())
for test_case in range(1, T + 1):
    n, L = map(int, input().split())
    li = []
    for _ in range(n):
        li.append(list(map(int, input().split())))
    total_score = 0
    dfs(0, 0, 0)
    print("#{} {}".format(test_case, total_score))