import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


dy = [-1, -1,  0, 1, 1,  1,  0, -1]
dx = [ 0,  1,  1, 1, 0, -1, -1, -1]

def dfs(y, x):
	global visited, map_

	visited[y][x] = True

	for i in range(8):
		ny = y + dy[i]
		nx = x + dx[i]

		if (0 <= ny <= h) and (0 <= nx <= w):
			if map_[ny][nx] and not visited[ny][nx]:
				dfs(ny, nx)

while True:
	w, h = map(int, input().split())

	if w == 0 and h == 0:
		break

	map_ = [[False] * (w+1) for _ in range(h+1)]
	visited = [[False] * (w+1) for _ in range(h+1)]

	for y in range(1, h+1):
		row = list(map(int, input().split()))
		for x in range(1, w+1):
			map_[y][x] = (row[x-1] == 1)

	answer = 0
	for i in range(1, h+1):
		for j in range(1, w+1):
			if map_[i][j] and not visited[i][j]:
				dfs(i, j)
				answer += 1

	print(answer)


	
	