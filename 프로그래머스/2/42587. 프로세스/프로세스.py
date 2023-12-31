from collections import deque
def solution(priorities, location):
    resource = deque(enumerate(priorities))
    result = []
    while resource:
        q = resource.popleft()
        if any(q[1] < p[1] for p in resource):
            resource.append(q)
        else:
            result.append(q)
    
    for i in result:
        if i[0] == location:
            return result.index(i)+1