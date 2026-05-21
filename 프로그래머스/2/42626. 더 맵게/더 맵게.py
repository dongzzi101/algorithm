import heapq 

def solution(scoville, K):
    heapq.heapify(scoville)
    
    count = 0
    while scoville:
        min_val = heapq.heappop(scoville)
        
        if min_val >= K:
            return count
        
        if len(scoville) == 0:
            return -1
        
        next_min_val = heapq.heappop(scoville)
        new_val = min_val + (next_min_val * 2)
        heapq.heappush(scoville, new_val)
        count += 1
    
    return -1