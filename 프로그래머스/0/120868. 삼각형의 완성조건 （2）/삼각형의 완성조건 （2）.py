def solution(sides):
    sides.sort()
    max_side = []
    max_anon = []
    for side in range(1, sides[-1]+1):
        if sides[0] + side > sides[-1]:
            max_side.append(side)
            
    for side in range(sides[-1], sum(sides)):
        if sides[-1] < side:
            max_anon.append(side)
    return len(max_side) + len(max_anon)