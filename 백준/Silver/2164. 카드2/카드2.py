from collections import deque

n = int(input())

q = deque(range(1, n+1))

while q:
	if len(q) == 1:
		print(*q)
		break

	q.popleft()
	q.append(q.popleft())
