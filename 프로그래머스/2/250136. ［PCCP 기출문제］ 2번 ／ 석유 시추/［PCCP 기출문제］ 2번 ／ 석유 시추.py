from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    
    visited = [[False] * m for _ in range(n)]
    
    col_sum = [0] * m
    
    def bfs(y, x):
        q = deque([(y, x)])
        visited[y][x] = True
        
        count = 1
        cols = set([x])  
        
        while q:
            cy, cx = q.popleft()
            
            for d in range(4):
                ny = cy + dy[d]
                nx = cx + dx[d]
                
                if 0 <= ny < n and 0 <= nx < m:
                    if not visited[ny][nx] and land[ny][nx] == 1:
                        visited[ny][nx] = True
                        q.append((ny, nx))
                        count += 1
                        cols.add(nx)
        
        return count, cols
    
    for y in range(n):
        for x in range(m):
            if land[y][x] == 1 and not visited[y][x]:
                size, cols = bfs(y, x)
                
                for c in cols:
                    col_sum[c] += size
    
    return max(col_sum)