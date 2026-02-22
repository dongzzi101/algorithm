import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(s):
	global visited, adjs, answer, order

	visited[s] = True
	answer[s] = order
	order += 1

	for adj in adjs[s]:
		if not visited[adj]:
			dfs(adj)


N, M, R = map(int, input().split())

adjs = [[] for _ in range(N+1)]

for _ in range(M):
	a, b = map(int,input().split())
	adjs[a].append(b)
	adjs[b].append(a)


for i in range(1, N+1):
	adjs[i].sort()

order = 1
answer = [0] * (N+1)
visited = [False] * (N+1)

dfs(R)

for i in range(1, N+1):
	print(answer[i])