def solution(lottos, win_nums):
    l = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    count = 0
    for i in lottos:
        if i in win_nums:
            count += 1
    return [l[count+lottos.count(0)], l[count]]