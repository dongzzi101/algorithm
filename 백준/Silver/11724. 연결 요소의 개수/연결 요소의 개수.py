import sys
input = sys.stdin.readline

from collections import deque

n, nn = map(int, input().split())

adjs = [[] for _ in range(n+1)]

for _ in range(nn):
	a, b = map(int, input().split())
	adjs[a].append(b)
	adjs[b].append(a)

visited = [False] * (n+1)

def bfs(node):
	q = deque()
	q.append(node)
	visited[node] = True

	while q:
		node = q.popleft()

		for adj in adjs[node]:
			if not visited[adj]:
				q.append(adj)
				visited[adj] = True

count = 0
for i in range(1, n+1):
	if not visited[i]:
		bfs(i)
		count += 1

print(count)


