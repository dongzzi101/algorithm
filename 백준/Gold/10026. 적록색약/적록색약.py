import sys
sys.setrecursionlimit(10**6)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x):
    visited[y][x] = True
    color = board[y][x]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < N:
            if not visited[ny][nx] and board[ny][nx] == color:
                dfs(ny, nx)

N = int(input())
board = [list(input().strip()) for _ in range(N)]

visited = [[False]* N for _ in range(N)]
count1 = 0

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            dfs(y, x)
            count1 += 1

for y in range(N):
    for x in range(N):
        if board[y][x] == 'G':
            board[y][x] = 'R'

visited = [[False]* N for _ in range(N)]
count2 = 0

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            dfs(y, x)
            count2 += 1

print(count1, count2)