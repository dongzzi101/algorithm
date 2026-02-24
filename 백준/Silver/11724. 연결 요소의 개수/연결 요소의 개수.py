import sys
input = sys.stdin.readline

def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()
        for adj in adjs[node]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)

N, M = map(int, input().split())

adjs = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjs[a].append(b)
    adjs[b].append(a)

visited = [False] * (N+1)

num_of_cc = 0
for node in range(1, N+1):
    if not visited[node]:
        dfs(node)
        num_of_cc += 1

print(num_of_cc)