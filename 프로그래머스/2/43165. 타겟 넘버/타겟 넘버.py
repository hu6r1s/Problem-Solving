from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([0, numbers[0]])
    queue.append([0, -numbers[0]])
    while queue:
        idx, temp = queue.popleft()
        idx += 1
        if idx < len(numbers):
            queue.append([idx, temp + numbers[idx]])
            queue.append([idx, temp - numbers[idx]])
        else:
            if temp == target:
                answer += 1
    return answer