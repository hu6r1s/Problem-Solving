def solution(order):
    bojo = []
    main = [i for i in range(1, len(order) + 1)]
    result = 0
    idx = 0
    for box in range(1, len(order)+1):
        bojo.append(box)
        
        while bojo and bojo[-1] == order[idx]:
            bojo.pop()
            result += 1
            idx += 1
    return result
            