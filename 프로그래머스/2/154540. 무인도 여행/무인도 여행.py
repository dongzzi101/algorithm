from collections import deque

def solution(maps):
    answer = []
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    def bfs(start_y, start_x):
        result = int(maps[start_y][start_x])

        q = deque()
        q.append((start_y, start_x))
        visited[start_y][start_x] = True
        
        
        while q:
            y, x = q.popleft()
            
            for i in range(4):
                ny = dy[i] + y
                nx = dx[i] + x

                if (0 <= ny < len(maps) and (0 <= nx < len(maps[0]))):
                    if not visited[ny][nx] and maps[ny][nx] != 'X':
                        q.append((ny, nx))
                        visited[ny][nx] = True 
                        result += int(maps[ny][nx])
        
        return result
    
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] != 'X':
                if not visited[y][x]:
                    total_count = bfs(y,x)
                    answer.append(total_count)
    if len(answer) == 0:
        return [-1]
    
    return sorted(answer)