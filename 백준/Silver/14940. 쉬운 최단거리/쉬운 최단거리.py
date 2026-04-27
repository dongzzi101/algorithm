from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def find_target():
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 2:
                return y, x

sy, sx = find_target()

q = deque()
q.append((sy, sx))

dist_map = [[-1] * m for _ in range(n)]
dist_map[sy][sx] = 0

visited = [[False] * m for _ in range(n)]
visited[sy][sx] = True

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

while q:
    y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m:
            if not visited[ny][nx] and graph[ny][nx] != 0:
                visited[ny][nx] = True
                dist_map[ny][nx] = dist_map[y][x] + 1
                q.append((ny, nx))

for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            print(0, end=' ')
        else:
            print(dist_map[y][x], end=' ')
    print()