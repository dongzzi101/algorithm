import heapq

def solution(N, road, K):
    adjs = [[] for _ in range(N+1)]
    
    for a, b, c in road:
        adjs[a].append((b, c))
        adjs[b].append((a, c))
    
    dist = [float('inf')] * (N+1)
    dist[1] = 0
    
    heap = [(0, 1)]  
    
    while heap:
        time, now = heapq.heappop(heap)
        
        if time > dist[now]:
            continue
        
        for nxt, cost in adjs[now]:
            new_time = time + cost
            
            if new_time < dist[nxt]:
                dist[nxt] = new_time
                heapq.heappush(heap, (new_time, nxt))
    
    return sum(1 for d in dist if d <= K)