from collections import deque


def bfs(si, sj):
	q = deque()
	q.append((si,sj))
	vistited[si][sj] = True	
	count = 1

	while q:
		ci, cj = q.popleft()

		for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
			ni, nj = ci+di, cj+dj

			if (0<= ni < N and 0 <= nj < N):
				if matrix[ni][nj] == 1 and  not vistited[ni][nj]:
					q.append((ni, nj))
					vistited[ni][nj] = True
					count += 1
	return count


N = int(input())
matrix = [ list(map(int, input())) for _ in range(N) ]

vistited = [[0] * N for _ in range(N)]
ans = []

for i in range(N):
	for j in range(N):
		if matrix[i][j] == 1 and vistited[i][j] == 0:
			ans.append(bfs(i, j))

ans.sort()
print(len(ans), *ans, sep='\n')








