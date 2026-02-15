from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    q = deque()
    visited = [[False] * m for _ in range(n)]        

    q.append((0,0,1))
    visited[0][0] = True
    
    while q:
        y, x, dist = q.popleft()
        
        if y == n - 1 and x == m -1:
            return dist
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if (0 <= ny < n) and (0 <= nx < m):
                if not visited[ny][nx] and maps[ny][nx] == 1:
                    q.append((ny, nx, dist+1))    
                    visited[ny][nx] = True
    
    return -1