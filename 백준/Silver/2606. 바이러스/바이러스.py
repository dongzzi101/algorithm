from collections import deque

N = int(input())
edges = int(input())

adjs = [[] for _ in range(N+1)]


for _ in range(edges):
	a, b = map(int, input().split())
	adjs[a].append(b)
	adjs[b].append(a)

q = deque()
q.append(1)

visited = [False] * (N+1)
visited[1] = True

count = 0
while q:
	node = q.popleft()

	for adj in adjs[node]:
		if not visited[adj]:
			count += 1
			q.append(adj)
			visited[adj] = True

print(count)

