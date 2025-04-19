def solution(dirs):
    x, y, count = 0, 0, set()
    d = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }
    
    for dir in dirs:
        dx, dy = d[dir]
        nx = x + dx
        ny = y + dy
        if nx > 5 or nx < -5 or ny > 5 or ny < -5:
            continue
        
        count.add(((x, y), (nx, ny)))
        count.add(((nx, ny), (x, y)))
        x = nx
        y = ny
    return len(count) // 2