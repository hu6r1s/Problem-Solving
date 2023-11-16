T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    li_90 = [[0] * n for _ in range(n)]
    li_180 = [[0] * n for _ in range(n)]
    li_270 = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            li_90[i][j] = li[n-j-1][i]

    for i in range(n):
        for j in range(n):
            li_180[i][j] = li[n-i-1][n-j-1]

    for i in range(n):
        for j in range(n):
            li_270[i][j] = li[j][n-i-1]

    print("#{}" .format(test_case))
    for i in range(n):
        for a in range(n):
            print(li_90[i][a], end="")
        print(end=" ")
        for b in range(n):
            print(li_180[i][b], end="")
        print(end=" ")
        for c in range(n):
            print(li_270[i][c], end="")
        print(end=" ")
        print()