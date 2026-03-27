from collections import deque

N = int(input())

adjs = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    adjs[a].append(b)
    adjs[b].append(a)

q = deque([1])

visited = [False] * (N+1)
visited[1] = True

parents = [0] * (N+1)

while q:
    node = q.popleft()

    for adj in adjs[node]:
        if not visited[adj]:
            parents[adj] = node
            visited[adj] = True
            q.append(adj)

for i in range(2, N+1):
    print(parents[i])