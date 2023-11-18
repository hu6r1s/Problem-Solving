def dfs(c, v):
    global count
    count = max(count, len(v))

    for i in graph[c]:
        if i not in v:
            dfs(i, v+[i])

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input(). split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    count = 0
    for s in range(1, n+1):
        dfs(s, [s])

    print("#{} {}".format(test_case, count))