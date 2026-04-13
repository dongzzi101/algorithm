from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    def bfs(sy, sx, target):
        q = deque()
        q.append((sy, sx, 0))
        visited = [[False] * m for _ in range(n)]
        visited[sy][sx] = True
        
        while q:
            y, x, dist = q.popleft()
            
            if maps[y][x] == target:
                return dist
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if 0 <= ny < n and 0 <= nx < m:
                    if not visited[ny][nx] and maps[ny][nx] != 'X':
                        visited[ny][nx] = True
                        q.append((ny, nx, dist+1))
        
        return -1
    
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 'S':
                sy, sx = y, x
            if maps[y][x] == 'L':
                ly, lx = y, x
    
    t1 = bfs(sy, sx, 'L')
    if t1 == -1:
        return -1
    
    t2 = bfs(ly, lx, 'E')
    if t2 == -1:
        return -1
    
    return t1 + t2