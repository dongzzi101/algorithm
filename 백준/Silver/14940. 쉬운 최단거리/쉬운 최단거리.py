from collections import deque

n, m = map(int, input().split())


lands = [list(map(int, input().split())) for _ in range(n)]

def find_number_two():
	for y in range(n):
		for x in range(m):
			if lands[y][x] == 2:
				return y, x


q = deque()
y, x = find_number_two()
lands[y][x] = 0
q.append((y, x))


visited = [[False] * m for _ in range(n)]
visited[y][x] = True


dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

while q:

	y, x = q.popleft()

	for i in range(4):
		ny = y + dy[i]
		nx = x + dx[i]

		if (0 <= ny < n) and (0 <= nx < m):
			if not visited[ny][nx]:
				if lands[ny][nx] != 0:
					lands[ny][nx] = (lands[y][x] + 1)
					q.append((ny, nx))
					visited[ny][nx] = True

for y in range(n):
    for x in range(m):
        if lands[y][x] == 1 and not visited[y][x]:
            lands[y][x] = -1	

for land in lands:
	print(*land)

