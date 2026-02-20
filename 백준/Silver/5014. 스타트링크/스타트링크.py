from collections import deque

def bfs(start, end):
	q = deque()
	visit = [0] * (F + 1)
	
	q.append(start)
	visit[start] = 1

	while q:
		cur = q.popleft()
		
		if cur == end:
			return visit[cur] - 1

		for next_node in (cur + U, cur - D):
			if 1<= next_node <= F and visit[next_node] == 0:
					q.append(next_node)
					visit[next_node] = visit[cur] + 1
					
	return -1


F, S, G, U, D = map(int, input().split())


ans = bfs(S, G)

if ans == -1:
    print("use the stairs")
else:
    print(ans)
