from collections import deque

n, m = map(int, input().split())

board = [ [0] + list(map(int, input().split()))  for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def find_target(num):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 2:
                return y, x

y, x = find_target(2)

q = deque()
q.append((y, x))

dist = [[-1]*(m+1) for _ in range(n+1)]
visited = [[False] * (m+1) for _ in range(n+1)]

visited[y][x] = True
dist[y][x] = 0

while q:
    y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]  
        nx = x + dx[i]  

        if 0 <= ny < n and 1 <= nx <= m:  
            if board[ny][nx] != 0 and not visited[ny][nx]:  
                dist[ny][nx] = dist[y][x] + 1
                visited[ny][nx] = True
                q.append((ny, nx))

for i in range(n):
    for j in range(1, m+1):
        if board[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()