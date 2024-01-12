import math

def solution(number, limit, power):
    li = []
    for i in range(1, number+1):
        count = 0
        for j in range(1, int(math.sqrt(i))+1):
            if i % j == 0:
                count += 1
                if j ** 2 != i:
                    count += 1
        li.append(count)
    for i in range(len(li)):
        if li[i] > limit:
            li[i] = power
    return sum(li)