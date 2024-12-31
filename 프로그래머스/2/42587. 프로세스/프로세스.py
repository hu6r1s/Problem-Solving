from collections import deque
def solution(priorities, location):
    queue = deque(enumerate(priorities))
    process = []
    
    while queue:
        q = queue.popleft()
        if any(q[1] < v[1] for v in queue):
            queue.append(q)
        else:
            process.append(q[0])
    
    for p in process:
        if p == location:
            return process.index(p) + 1