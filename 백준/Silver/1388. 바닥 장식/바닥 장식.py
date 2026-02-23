import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(y, x):
    visited[y][x] = True

    if map_[y][x] == '-':
        if x + 1 <= M and not visited[y][x+1] and map_[y][x+1] == '-':
            dfs(y, x+1)

    elif map_[y][x] == '|':
        if y + 1 <= N and not visited[y+1][x] and map_[y+1][x] == '|':
            dfs(y+1, x)


N, M = map(int, input().split())

map_ = [[0] * (M+1) for _ in range(N+1)]
visited = [[False] * (M+1) for _ in range(N+1)]

for y in range(1, N+1):
    row = input().strip()
    for x in range(1, M+1):
        map_[y][x] = row[x-1]

answer = 0

for y in range(1, N+1):
    for x in range(1, M+1):
        if not visited[y][x]:
            dfs(y, x)
            answer += 1

print(answer)