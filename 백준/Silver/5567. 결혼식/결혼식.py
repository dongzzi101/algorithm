from collections import deque

N = int(input())
M = int(input())

adjs = [[] for _ in range(N+1)]

for _ in range(M):
	a, b = map(int, input().split())
	adjs[a].append(b)
	adjs[b].append(a)


visited= [False] * (N+1)

q = deque()
q.append((1, 0))
visited[1] = True

count = 0

while q:
	node, depth = q.popleft()

	if depth == 2:
		continue

	for adj in adjs[node]:
		if not visited[adj]:
			q.append((adj, depth+1))
			visited[adj] = True
			count += 1

print(count)

