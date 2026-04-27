from collections import deque

n, m = map(int, input().split())

maze = [list(map(int, input())) for _ in range(n)]

q = deque()
q.append((0, 0, 1))

visited =[[False] * m for _ in range(n)]
visited[0][0] = True

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

while q:
	y, x, dist = q.popleft()

	if (y == (n - 1)) and (x == (m - 1)):
		print(dist)

	for i in range(4):
		ny = y + dy[i]
		nx = x + dx[i]

		if (0 <= ny < n) and (0 <= nx < m):
			if not visited[ny][nx] and maze[ny][nx] == 1:
				q.append((ny, nx, dist+1))
				visited[ny][nx] = True




