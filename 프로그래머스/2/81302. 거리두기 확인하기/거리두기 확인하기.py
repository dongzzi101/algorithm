from collections import deque

def solution(places):
    def bfs(board, y, x):
        q = deque()
        q.append((y, x, 0))
        
        visited = [[False] * 5 for _ in range(5)]
        visited[y][x] = True
        
        dy = [1, -1, 0, 0]
        dx = [0, 0, 1, -1]
        
        while q:
            cy, cx, dist = q.popleft()
            
            if dist >= 1 and board[cy][cx] == "P":
                return False
            
            if dist == 2:
                continue
            
            for d in range(4):
                ny = cy + dy[d]
                nx = cx + dx[d]
                
                if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx]:
                    if board[ny][nx] != "X":
                        visited[ny][nx] = True
                        q.append((ny, nx, dist + 1))
        
        return True
    
    
    answer = []
    
    for place in places:
        valid = True
        
        for y in range(5):
            for x in range(5):
                if place[y][x] == "P":
                    if not bfs(place, y, x):
                        valid = False
                        break
            if not valid:
                break
        
        answer.append(1 if valid else 0)
    
    return answer