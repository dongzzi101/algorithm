from collections import deque

def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    
    q = deque()
    visited = [[False] * m for _ in range(n)]
    
    q.append((0, 0, 1))
    visited[0][0] = True
    
    dy = [1,0, -1, 0]
    dx = [0, 1, 0, -1]
    while q:
        y, x, dist = q.popleft()
        
        if y+1 == n and x+1== m:
            return dist 
        
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx]:
                    if maps[ny][nx] == 1:
                        q.append((ny, nx, dist+1))
                        visited[ny][nx] = True
                        
    return -1 