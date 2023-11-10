T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    li = [[0] * n for _ in range(n)]
    li[0][0] = 1
    for i in range(1, n):
        for j in range(n):
            if j == 0:
                li[i][j] = 1
            else:
                li[i][j] = li[i - 1][j - 1] + li[i - 1][j]
    print("#{}" .format(test_case))
    for i in range(n):
        for j in range(n):
            if li[i][j]:
            	print(li[i][j], end=" ")
        print()