n, m = map(int, input().split())
li1 = [list(map(int, input().split())) for _ in range(n)]
li2 = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        print(li1[i][j] + li2[i][j], end=" ")
    print()