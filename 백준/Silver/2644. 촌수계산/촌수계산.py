def dfs(start, depth):
    global answer

    if start == end:
        answer = depth
        return True

    visited[start] = True

    for adj in adjs[start]:
        if not visited[adj]:
            if dfs(adj, depth + 1):
                return True

    return False


N = int(input())
start, end = map(int, input().split())
M = int(input())
adjs = [[] for _ in range(N+1)]

for _ in range(M):
	x, y = map(int, input().split())
	adjs[x].append(y)
	adjs[y].append(x)

visited = [False] * (N+1)
answer = -1
count = 0

dfs(start, 0)

print(answer)