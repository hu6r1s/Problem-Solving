def solution(keyinput, board):
    direct = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right': [1, 0]}
    x, y = board
    x_v, y_v = 0, 0
    for key in keyinput:
        if abs(x_v + direct[key][0]) > x // 2 or abs(y_v + direct[key][1]) > y // 2:
            continue
        x_v += direct[key][0]
        y_v += direct[key][1]
    
    return [x_v, y_v]