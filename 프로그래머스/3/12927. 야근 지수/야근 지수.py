import heapq

def solution(n, works):
    # if sum(works) <= n:
    #     return 0
    # else:
    #     for _ in range(n):
    #         works.sort(reverse=True)
    #         works[0] -= 1
    #     return sum([work ** 2 for work in works])
    
    if sum(works) <= n:
        return 0
    
    max_heap = [-w for w in works]
    heapq.heapify(max_heap)

    for _ in range(n):
        max_work = -heapq.heappop(max_heap)
        max_work -= 1
        heapq.heappush(max_heap, -max_work)

    return sum(work ** 2 for work in max_heap)