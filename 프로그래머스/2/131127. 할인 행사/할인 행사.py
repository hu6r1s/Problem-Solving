def solution(want, number, discount):
    count = 0
    for i in range(len(discount)-sum(number)+1):
        if all(number[w] == discount[i:i+sum(number)].count(want[w]) for w in range(len(want))):
            count += 1
    return count