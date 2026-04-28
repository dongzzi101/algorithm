from collections import deque

n = int(input())
nn = int(input())

adjs = [[] for _ in range(n+1)]

for _ in range(nn):
	a, b = map(int, input().split())
	adjs[a].append(b)
	adjs[b].append(a)

q = deque()
q.append(1)

visited = [False] * (n+1)
visited[1] = True

count = 0

while q:
	node = q.popleft()

	for adj in adjs[node]:
		if not visited[adj]:
			q.append(adj)
			count += 1
			visited[adj] = True	

print(count)