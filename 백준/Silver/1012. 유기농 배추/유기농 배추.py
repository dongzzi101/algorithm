from collections import deque


dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs(sy, sx):
	q = deque()
	q.append((sy, sx))
	board[sy][sx] = 0

	while q:
		y, x = q.popleft()

		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if (0 <= ny < N) and (0 <= nx < M) and board[ny][nx] == 1:
				board[ny][nx] = 0
				q.append((ny, nx))


T = int(input())

for _ in range(T):
	M, N, K = map(int, input().split())
	board = [[0] * M for _ in range(N)]

	for _ in range(K):
		x, y = map(int, input().split())
		board[y][x] = 1

	count = 0

	for i in range(N):
		for j in range(M):
			if board[i][j] == 1:
				bfs(i, j)
				count += 1

	print(count)


