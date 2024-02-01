def solution(brown, yellow):
    total = brown + yellow
    for b in range(1, total+1):
        if total % b == 0:
            a = total // b
            if a >= b:
                if a * b - 2 * a - 2 * b + 4 == yellow:
                    return [a, b]