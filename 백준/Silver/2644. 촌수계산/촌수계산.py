from collections import deque

def bfs(start, end):
	q = deque()
	
	q.append(start)
	visited[start] = True

	while q:
		c = q.popleft()

		if c == end:
			return visited[end] - 1

		for n in adjs[c]:
			if not visited[n]:
				q.append(n)
				visited[n] += visited[c] + 1

	return -1


n = int(input())
start, end = map(int, input().split())

nn = int(input())

adjs = [[] for _ in range(n + 1)]


for _ in range(nn):
	a, b = map(int, input().split())
	adjs[a].append(b)
	adjs[b].append(a)


visited = [False] * (n + 1)

ans = bfs(start, end)
print(ans)
