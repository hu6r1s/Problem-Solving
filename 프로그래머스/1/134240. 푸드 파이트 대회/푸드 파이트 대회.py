def solution(food):
    s = ""
    for index, f in enumerate(food[1:]):
        s += str(index+1) * (f // 2)
    return s + "0" + s[::-1]