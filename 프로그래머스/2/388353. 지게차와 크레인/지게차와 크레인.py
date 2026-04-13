from collections import deque

def solution(storage, requests):
    storage = [list(row) for row in storage]
    
    n = len(storage)
    m = len(storage[0])
    
    def remove_storage(request):
        nonlocal storage
        
        new = [[0] * (m + 2) for _ in range(n + 2)]
        for i in range(n):
            for j in range(m):
                new[i+1][j+1] = storage[i][j]
        
        if len(request) >= 2:
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if new[i][j] == request[0]:
                        new[i][j] = 0
        
        else:
            visited = [[False]*(m+2) for _ in range(n+2)]
            q = deque([(0, 0)])
            visited[0][0] = True
            
            to_remove = []
            
            while q:
                y, x = q.popleft()
                
                for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ny, nx = y+dy, x+dx
                    
                    if 0 <= ny < n+2 and 0 <= nx < m+2 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        
                        if new[ny][nx] == 0:
                            q.append((ny, nx))
                        
                        elif new[ny][nx] == request:
                            to_remove.append((ny, nx))
            
            for y, x in to_remove:
                new[y][x] = 0
        
        for i in range(n):
            for j in range(m):
                storage[i][j] = new[i+1][j+1]
    
    for request in requests:
        remove_storage(request)
    
    count = sum(row.count(0) for row in storage)
    return n*m - count