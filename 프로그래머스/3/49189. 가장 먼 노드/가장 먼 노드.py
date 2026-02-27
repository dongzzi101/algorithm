from collections import deque
    
def solution(n, edge):
    adjs = [[] for _ in range(n+1)]
    
    for a, b in edge:
        adjs[a].append(b)
        adjs[b].append(a)
    
    distance = [-1] * (n + 1)
    q = deque()
    q.append(1)
    distance[1] = 0
    
    while q:
        node = q.popleft()
        
        for ajd in adjs[node]:
            if distance[ajd] == -1:
                distance[ajd] = distance[node] + 1 
                q.append(ajd)
     
    max_dist = max(distance)
    answer = distance.count(max_dist)
    return answer