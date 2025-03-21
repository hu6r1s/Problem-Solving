def solution(people, limit):
    result = 0
    start = 0
    end = len(people) - 1
    people.sort()
    while start <= end:
        if people[start] + people[end] <= limit:
            result += 1
            start += 1
            end -= 1
        else:
            result += 1
            end -= 1
    return result