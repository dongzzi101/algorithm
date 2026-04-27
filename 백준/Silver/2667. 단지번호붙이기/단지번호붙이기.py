from collections import deque

n = int(input())

graph = [list(map(int, input())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

dy = [1, 0 , -1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
	q = deque()
	q.append((y, x))
	visited[y][x] = True
	count = 1
	
	while q:
		y, x = q.popleft()

		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0 <= ny < n and 0 <= nx < n:
				if not visited[ny][nx] and graph[ny][nx] == 1:
					q.append((ny, nx))
					visited[ny][nx] = True
					count += 1

	return count

result = []
for y in range(n):
	for x in range(n):
		if graph[y][x] == 1 and not visited[y][x]:
			count = bfs(y, x)
			result.append(count)

result.sort()
print(len(result))
for r in result:
	print(r)
