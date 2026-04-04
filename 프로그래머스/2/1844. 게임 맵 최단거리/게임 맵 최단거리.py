from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    
    new_maps = [[0] * (col + 1)]
    for r in maps:
        new_maps.append([0] + r)
    
    if new_maps[1][1] == 0:
        return -1
    
    q = deque()
    q.append((1, 1, 1))
    
    visited = [[False] * (col+1) for _ in range(row+1)]
    visited[1][1] = True
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    while q:
        y, x, dist = q.popleft()
        
        if y == row and x == col:
            return dist
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 1 <= ny <= row and 1 <= nx <= col:
                if not visited[ny][nx] and new_maps[ny][nx] != 0:
                    visited[ny][nx] = True
                    q.append((ny, nx, dist+1))
    
    return -1