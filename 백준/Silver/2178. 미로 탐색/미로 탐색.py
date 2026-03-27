from collections import deque

n, m = map(int, input().split())

board = [[0]*(m+1)]
for _ in range(n):
    board.append([0] + list(map(int, input())))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

q = deque()
q.append((1,1))

visited = [[False] * (m+1) for _ in range(n+1)]
visited[1][1] = True

dist = [[0]*(m+1) for _ in range(n+1)]
dist[1][1] = 1

while q:
	y, x = q.popleft()

	for i in range(4):
		ny = y + dy[i]
		nx = x + dx[i]

		if (1 <= ny <= n) and (1 <= nx <= m):
			if not visited[ny][nx] and board[ny][nx] == 1:
				q.append((ny, nx))
				visited[ny][nx] = True
				dist[ny][nx] = dist[y][x] + 1

print(dist[n][m])
