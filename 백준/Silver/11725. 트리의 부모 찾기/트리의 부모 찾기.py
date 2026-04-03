from collections import deque

n = int(input())


adjs = [[] * n for _ in range(n+1)]

for _ in range(n-1):
	a, b = map(int, input().split())
	adjs[a].append(b)
	adjs[b].append(a)

q = deque()
q.append(1)

visited = [False] * (n+1)
visited[1] = True

parents = [0] * (n+1)

while q:
	node = q.popleft()

	for adj in adjs[node]:
		if not visited[adj]:
			parents[adj] = node
			visited[adj] = True
			q.append(adj)


print(*parents[2:])