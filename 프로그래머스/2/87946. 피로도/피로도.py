from itertools import permutations

def solution(k, dungeons):
    result = 0
    for p in permutations(dungeons, len(dungeons)):
        count = 0
        nk = k
        for need, use in p:
            if nk >= need:
                nk -= use
                count += 1
        result = max(count, result)
    return result