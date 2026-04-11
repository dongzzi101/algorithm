import heapq

def solution(n, k, enemy):
    answer = 0
    
    if n >= sum(enemy):
        return len(enemy)
    
    if k >= len(enemy):
        return len(enemy)
    
    heap = []
    round = 0
    
    for i in range(len(enemy)):
        heapq.heappush(heap, enemy[i])
        
        if len(heap) > k:
            n -= heapq.heappop(heap)
        
        if n < 0:
            return round
        
        round += 1
    
    return round