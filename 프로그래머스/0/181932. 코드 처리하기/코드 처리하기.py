def solution(code):
    mode = 0
    ret = ''
    for idx in range(len(code)):
        if code[idx] == '1' and not mode:
            mode = 1
        elif code[idx] == '1' and mode:
            mode = 0
        
        if mode:
            if code[idx] != '1' and idx % 2:
                ret += code[idx]
        else:
            if code[idx] != '1' and not idx % 2:
                ret += code[idx]
    return ret if ret else 'EMPTY'