from collections import defaultdict

def solution(msg):
    d = defaultdict(int)
    for i in range(65, 91):
        d[chr(i)] = i - 64
    
    answer = []
    next_index = 27
    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = next_index
                next_index += 1
                msg = msg[i-1:]
                break
    return answer