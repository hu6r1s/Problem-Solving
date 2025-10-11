from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    cnt = 0
    sum1, sum2 = sum(queue1), sum(queue2)
    max = len(queue1) * 3
    
    while cnt < max:
        if sum1 == sum2:
            return cnt
        
        if sum1 < sum2:
            t = queue2.popleft()
            queue1.append(t)
            sum2 -= t
            sum1 += t
        else:
            t = queue1.popleft()
            queue2.append(t)
            sum1 -= t
            sum2 += t
            
        cnt += 1
        
    return -1

"""
deque 이용
앞의 원소를 빼서 다른 큐의 맨 뒤에 넣어줌
그리고 비교해서 합이 15이면 종료

10
1 2 1 2 1 2 1
"""
