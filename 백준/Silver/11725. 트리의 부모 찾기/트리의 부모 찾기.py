from collections import deque

N = int(input())

adjs_list = [[] for _ in range(N+1)]

for _ in range(N-1):
	a, b = map(int, input().split())
	adjs_list[a].append(b)
	adjs_list[b].append(a)

visited = [False] * (N+1)
parent = [0] * (N+1)

q = deque()
q.append(1)
visited[1] = True


while q:
	node = q.popleft()


	for cur_node in adjs_list[node]:

		if visited[cur_node]:
			continue

		parent[cur_node] = node
		q.append(cur_node)
		visited[cur_node] = True

for i in range(2, N+1):
	print(parent[i])