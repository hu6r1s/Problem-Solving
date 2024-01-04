import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    
    while True:
        if all(i >= K for i in scoville):
            return count
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
            
        count += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first+second*2)