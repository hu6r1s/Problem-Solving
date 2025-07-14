def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    ans1 = (y2 - y1) / (x2 - x1) == (y4 - y3) / (x4 - x3) 
    ans2 = (y3 - y1) / (x3 - x1) == (y4 - y2) / (x4 - x2)
    ans3 = (y4 - y1) / (x4 - x1) == (y2 - y3) / (x2 - x3)
    
    return 1 if ans1 or ans2 or ans3 else 0