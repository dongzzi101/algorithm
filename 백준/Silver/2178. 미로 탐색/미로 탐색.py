from collections import deque

N, M = map(int, input().split())
maps = [ list(map(int, input()))  for _ in range(N)]


visited = [[False] * M for _ in range(N)]

q = deque()
q.append((0,0))

visited[0][0] = True

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

while q:
	y, x = q.popleft()

	for i in range(4):
		ny = y + dy[i]
		nx = x + dx[i]

		if 0 <= nx < M and 0 <= ny < N:
			if maps[ny][nx] == 1:
				maps[ny][nx] = maps[y][x] + 1
				q.append((ny, nx))

print(maps[N-1][M-1])