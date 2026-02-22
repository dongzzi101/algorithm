import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline




def dfs(idx):
	global visited, answer, adjs

	visited[idx] = True

	for adj in adjs[idx]:		
		if not visited[adj]:
			answer[adj] = idx
			visited[adj] = True
			dfs(adj)


N = int(input())

adjs = [[] for _ in range(N+1)]
answer = [0] * (N+1)
visited = [False] * (N+1)

for _ in range(N-1):
	a, b = map(int, input().split())
	adjs[a].append(b)
	adjs[b].append(a)

dfs(1)

for i in range(2, N+1):
	print(answer[i])