from collections import deque

n = int(input())
nn = int(input())

adjs = [[] * (n+1) for _ in range(n+1)]

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
	cur = q.popleft()

	for adj in adjs[cur]:
		if not visited[adj]:
			q.append(adj)
			visited[adj] = True
			count += 1

print(count)
