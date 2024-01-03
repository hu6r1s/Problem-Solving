def solution(array, commands):
    result = []
    for cmd in commands:
        result.append(sorted(array[cmd[0]-1:cmd[1]])[cmd[2]-1])
    return result