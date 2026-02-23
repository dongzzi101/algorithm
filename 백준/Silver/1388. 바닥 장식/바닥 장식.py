import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(y, x):

	global visited, map_

	visited[y][x] = True

	if map_[y][x] == 0:
		nx = x + 1
		if nx <= M and not visited[y][nx] and map_[y][nx] == 0:
			dfs(y, nx)

	else:
		ny = y + 1
		if ny <= N and not visited[ny][x] and map_[ny][x] == 1:
			dfs(ny, x)



N, M = map(int, input().split())

map_ = [[False] * (M+1) for _ in range(N+1)]
visited = [[False] * (M+1) for _ in range(N+1)]
answer = 0

for y in range(1, N+1):
	row = input()
	for x in range(1, M+1):
		if row[x-1] == "-":
			map_[y][x] = 0
		else:
			map_[y][x] = 1


for y in range(1, N+1):
	for x in range(1, M+1):
		if not visited[y][x]:
			dfs(y, x)
			answer += 1

print(answer)


