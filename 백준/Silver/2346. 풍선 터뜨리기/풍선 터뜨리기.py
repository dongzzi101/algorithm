from collections import deque

N = int(input())
pos = list(map(int, input().split()))

q = deque()

for i in range(N):
    q.append((i+1, pos[i]))

result = []

while q:
    balloon, move = q.popleft()
    result.append(balloon)

    if not q:
    	break

    if move > 0:
        for _ in range(move - 1):
            q.append(q.popleft())
    else:
        for _ in range(abs(move)):
            q.appendleft(q.pop())

print(*result)