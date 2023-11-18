T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    m = n // 2
    li = [list(map(int, input())) for _ in range(n)]
    result = 0
    # for i in range(n):
    #     if i <= m:
    #         for j in range(m-i, m+i+1):
    #             result += li[i][j]
    #     else:
    #         for j in range(i-m, n-(i-m)):
    #             result += li[i][j]
    s = e = m
    for i in range(n):
        for j in range(s, e + 1):
            result += li[i][j]
        if i < m:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print("#{} {}" .format(test_case, result))