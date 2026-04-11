from collections import deque


def solution(maps):
    answer = []
    
    dy = [1, 0 , -1 ,0]
    dx = [0, 1, 0, -1]
    
    row = len(maps[0])
    col = len(maps)
    
    q = deque()
    visited = [[False] * row for _ in range(col)]
    
    def bfs(y, x):
        total = int(maps[y][x])  # 시작점 포함

        q = deque()
        q.append((y, x))
        visited[y][x] = True

        while q:
            y, x = q.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if (0 <= ny < col) and (0 <= nx < row):
                    if maps[ny][nx] != "X" and not visited[ny][nx]:
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        total += int(maps[ny][nx])

        return total
        
    for y in range(col):
        for x in range(row):
            if maps[y][x] != "X" and not visited[y][x]:
                    total = bfs(y, x)
                    answer.append(total)
    answer.sort()
    if len(answer) == 0:
        return [-1]
    
    return answer