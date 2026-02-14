from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())


matrix = [[0] * (M+1)]

for _ in range(N):
	row = [0] + list(map(int, input().split()))
	matrix.append(row)


for i in range(1, N+1):
	for j in range(1, M+1):
		if matrix[i][j] == 2:
			start_y, start_x = i, j

dist = [[-1]*(M+1) for _ in range(N+1)]


q = deque()
q.append((start_y, start_x))
dist[start_y][start_x] = 0

while q:
	y, x = q.popleft()

	for d in range(4):
		ny = y + dy[d]
		nx = x + dx[d]

		if 1 <= ny <= N and 1 <= nx <= M:
			if matrix[ny][nx] == 1 and dist[ny][nx] == -1:
				dist[ny][nx] = dist[y][x] + 1
				q.append((ny, nx))


for i in range(1, N+1):
	for j in range(1, M+1):
		if matrix[i][j] == 0:
			print(0, end=' ')
		else:
			print(dist[i][j], end=' ')
	print()