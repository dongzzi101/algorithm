from collections import deque

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0,1, 0,-1]



def bfs(sy, sx):
	q = deque()
	q.append((sy, sx))
	visited[sy][sx] = True  
	count = 1

	while q:
		y, x = q.popleft()

		for d in range(4):
			ny = y + dy[d]
			nx = x + dx[d]

			if 0 <= ny < N and 0 <= nx < N:
				if matrix[ny][nx] == 1 and not visited[ny][nx]:
					visited[ny][nx] = True
					q.append((ny, nx))
					count += 1
	return count

result = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for r in result:
	print(r)



