T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    li = [[0] * n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    count, x, y, dr = 1, 0, 0, 0
    li[x][y] = count

    while count < n ** 2:
        nx = x + dx[dr]
        ny = y + dy[dr]
        if nx <= -1 or ny <= -1 or nx >= n or ny >= n or li[nx][ny] != 0:
            dr = (dr + 1) % 4
        else:
            x, y = nx, ny
            count += 1
            li[x][y] = count

    print("#{}".format(test_case))
    for i in range(n):
        for j in range(n):
            print(li[i][j], end=" ")
        print()