import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(y, x):
	global visited, board, answer

	if board[y][x] == -1:
		answer = True
		return

	visited[y][x] = True
	move = board[y][x]

	ny = y + move
	nx = x + move

	if ny < N and not visited[ny][x]:
		dfs(ny, x)

	if nx < N and not visited[y][nx]:
		dfs(y, nx)

	

N = int(input())

board = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for y in range(N):
	row = input().split()
	for x in range(N):
		board[y][x] = int(row[x])

answer = False

dfs(0, 0)



print("HaruHaru" if answer else "Hing")