def solution(quiz):
    result = []
    for qu in quiz:
        q, a = qu.split(" = ")
        if eval(q) == int(a):
            result.append("O")
        else:
            result.append("X")
    return result