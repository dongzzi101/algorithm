import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(y, x):
    global answer

    vistied[y][x] = True

    if y == M:
        answer = True
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if map_[ny][nx] and not vistied[ny][nx]:
            dfs(ny, nx)


M, N = map(int, input().split())

MAX = 1000 + 10
map_ = [[False] * MAX for _ in range(MAX)]
vistied = [[False] * MAX for _ in range(MAX)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(1, M+1):
    row = input()
    for j in range(1, N+1):
        map_[i][j] = (row[j-1] == "0")

answer = False
for j in range(1, N+1):
    if map_[1][j]:
        dfs(1, j)

print("YES" if answer else "NO")