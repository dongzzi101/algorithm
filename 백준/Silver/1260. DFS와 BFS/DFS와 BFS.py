from collections import deque

def dfs(node):
	global adj_list, visited

	if visited[node]:
		return
	visited[node] = True

	print(node, end=' ')

	for adj_node in adj_list[node]:
		dfs(adj_node)


def bfs(snode):
	global adj_list, visited

	q = deque()
	q.append(snode)
	visited[snode] = True

	while q:
		node = q.popleft()
		print(node, end =' ')

		for adj_node in adj_list[node]:
			if visited[adj_node]:
				continue
			q.append(adj_node)
			visited[adj_node] = True




N, M, V = map(int, input().split())

adj_list = [[] for _ in range(N+1)]
for _ in range(M):
	a, b = map(int, input().split())
	adj_list[a].append(b)
	adj_list[b].append(a)

for node in range(1, N+1):
	adj_list[node].sort()

visited = [False] * (N+1)
dfs(V)
print()

visited = [False] * (N+1)
bfs(V)
print()


