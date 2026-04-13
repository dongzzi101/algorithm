from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    waiting_truck = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    current_weight = 0  
    
    while waiting_truck:
        time += 1
        
        out = bridge.popleft()
        current_weight -= out
        
        if current_weight + waiting_truck[0] <= weight:
            truck = waiting_truck.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)
    
    return time + bridge_length