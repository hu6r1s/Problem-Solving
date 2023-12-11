n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
result = []
for i in range(n - 7):
    for j in range(m - 7):
        w_index = 0
        b_index = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != "W":
                        w_index += 1
                    else:
                        b_index += 1
                else:
                    if board[a][b] != "W":
                        b_index += 1
                    else:
                        w_index += 1
        result.append(w_index)
        result.append(b_index)
print(min(result))