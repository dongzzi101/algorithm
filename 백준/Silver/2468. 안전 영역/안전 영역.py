from collections import deque


def bfs(si, sj, h):
	q = deque()

	q.append((si, sj))
	visit[si][sj] = 1

	while q:
		ci, cj = q.popleft()

		for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
			ni, nj = ci+di, cj+dj
			if 0<= ni < N and 0 <= nj < N and visit[ni][nj] == 0 and arr[ni][nj] > h:
				q.append((ni, nj))
				visit[ni][nj] = 1


def solve(h):
	count = 0
	for i in range(N):
		for j in range(N):
			if visit[i][j] == 0 and arr[i][j] > h:
				bfs(i, j, h)
				count += 1

	return count



N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for h in range(100):
	visit = [[0] * N for _ in range(N)]
	ans = max(ans, solve(h))

print(ans)


