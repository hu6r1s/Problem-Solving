H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H + X)]

A = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        A[i][j] = B[i][j]

for i in range(X, H):
    for j in range(Y, W):
        A[i][j] = B[i][j] - A[i - X][j - Y]

for row in A:
    print(' '.join(map(str, row)))
