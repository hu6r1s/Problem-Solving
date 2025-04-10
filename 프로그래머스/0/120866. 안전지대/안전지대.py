def solution(board):
    dx, dy = [-1, 1, 0, 0, -1, 1, 1, -1], [0, 0, -1, 1, 1, 1, -1, -1]
    
    boom = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]:
                boom.append((i, j))
    for x, y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board):
                continue
            board[nx][ny] = 1
            
    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if not board[i][j]:
                count += 1
    return count
                    