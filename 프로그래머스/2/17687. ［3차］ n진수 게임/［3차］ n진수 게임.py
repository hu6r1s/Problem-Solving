def convert(n, base):
    digit = '0123456789ABCDEF'
    q, r = divmod(n, base)
    if q == 0:
        return digit[r]
    return convert(q, base) + digit[r]

def solution(n, t, m, p):
    string = ''
    result = ''
    for i in range(t*m):
        string += str(convert(i, n))
    
    while len(result) < t:
        result += string[p-1]
        p += m
    return result