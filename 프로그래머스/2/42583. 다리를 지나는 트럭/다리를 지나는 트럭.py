from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    count = 0
    curWeight = 0
    while truck_weights:
        count += 1
        curWeight -= bridge.popleft()
        
        if curWeight + truck_weights[0] <= weight:
            bridge.append(truck_weights[0])
            curWeight += truck_weights.pop(0)
        else:
            bridge.append(0)
        
    return count + bridge_length