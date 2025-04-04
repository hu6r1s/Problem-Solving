def solution(picture, k):
    result = []
    for i in range(len(picture)):
        for _ in range(k):
            result.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))
    return result