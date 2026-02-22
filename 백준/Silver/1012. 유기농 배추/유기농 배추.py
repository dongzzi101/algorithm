import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def dfs(y, x):
	global map_
	map_[y][x] = False

	for i in range(4):
		ny = y + dy[i]
		nx = x + dx[i]

		if map_[ny][nx]:
			dfs(ny, nx) 	


T = int(input())
MAX = 50 + 10

while T > 0:
	T -= 1
	 
	M, N, K = map(int, input().split())
	map_ = [[False] * MAX for _ in range(MAX)]
	
	for _ in range(K):
		x, y = map(int, input().split())
		map_[y + 1][x + 1] = True

	answer = 0
	for i in range(1, N+1):
		for j in range(1, M+1):
			if map_[i][j]:
				dfs(i, j)
				answer += 1

	print(answer)


