def solution(m, n, board):
    board = [list(b) for b in board]
    cnt = 0
    
    while True:
        remove = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != " ":
                    char = board[i][j]
                    if board[i][j+1] == char and board[i+1][j] == char and board[i+1][j+1] == char:
                        remove.add((i, j))
                        remove.add((i, j+1))
                        remove.add((i+1, j))
                        remove.add((i+1, j+1))

        if not remove:
            break
        
        cnt += len(remove)
        for x, y in remove:
            board[x][y] = " "

        for j in range(n):
            stack = []
            for i in range(m):
                if board[i][j] != " ":
                    stack.append(board[i][j])

            for i in range(m-1, -1, -1):
                if stack:
                    board[i][j] = stack.pop()
                else:
                    board[i][j] = " "
    
    print(board)
    return cnt