from collections import deque

def bfs(idx):
	global visited, adjs
	
	q = deque()
	q.append(idx)
	
	visited[idx] = True


	while q:
		node = q.popleft()
		print(node, end= ' ')

		for adj in adjs[node]:
			if not visited[adj]:	
				q.append(adj)
				visited[adj] = True



def dfs(idx):
	global visited, adjs

	visited[idx] = True

	print(idx, end=' ')

	for adj in adjs[idx]:
		if not visited[adj]:
			dfs(adj)



N, M, V = map(int, input().split())

adjs = [[] for _ in range(N+1)]

for _ in range(M):
	a, b = map(int, input().split())
	adjs[a].append(b)
	adjs[b].append(a)

for i in range(1, N+1):
	adjs[i].sort()


visited = [False] * (N+1)

dfs(V)
print()

visited = [False] * (N+1)
bfs(V)
