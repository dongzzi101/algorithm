from collections import deque

def solution(board):
    row = len(board)
    col = len(board[0])
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    for y in range(row):
        for x in range(col):
            if board[y][x] == "R":
                start_y, start_x = y, x
    
    q = deque()
    q.append((start_y, start_x, 0))
    
    visited = set()
    visited.add((start_y, start_x))
    
    while q:
        y, x, cnt = q.popleft()
        
        if board[y][x] == "G":
            return cnt
        
        for d in range(4):
            ny, nx = y, x
            
            while True:
                ny += dy[d]
                nx += dx[d]
                
                if not (0 <= ny < row and 0 <= nx < col) or board[ny][nx] == "D":
                    break
            
            ny -= dy[d]
            nx -= dx[d]
            
            if (ny, nx) not in visited:
                visited.add((ny, nx))
                q.append((ny, nx, cnt + 1))
    
    return -1