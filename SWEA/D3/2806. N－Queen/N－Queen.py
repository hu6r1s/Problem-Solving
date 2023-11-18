def dfs(v):
    global result
    if v == n:
        result += 1
        return
    for i in range(n):
        if v1[i] == v2[v+i] == v3[v-i] == 0:
            v1[i] = v2[v + i] = v3[v - i] = 1
            dfs(v+1)
            v1[i] = v2[v + i] = v3[v - i] = 0


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    v1, v2, v3 = [[0] * (n**2) for _ in range(3)]
    result = 0
    dfs(0)
    print("#{} {}" .format(test_case, result))