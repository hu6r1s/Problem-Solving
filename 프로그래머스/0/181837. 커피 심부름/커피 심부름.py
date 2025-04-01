def solution(order):
    result = 0
    for o in order:
        if 'americano' in o or 'anything' in o:
            result += 4500
        elif 'cafelatte' in o:
            result += 5000
    return result