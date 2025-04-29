def solution(lines):
    visited = [0] * 201
    cnt = 0
    
    for x1, x2 in lines:
        for i in range(x1 + 100, x2 + 100):
            visited[i] += 1
    return sum([1 for v in visited if v >= 2])