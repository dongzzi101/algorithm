N = int(input())
target = int(input())

graph = [[0]*N for _ in range(N)]

x, y = 0, 0
num = N * N

dir = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while num > 0:
    graph[y][x] = num

    if num == target:
        ty, tx = y, x

    num -= 1

    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx < 0 or nx >= N or ny < 0 or ny >= N or graph[ny][nx] != 0:
        dir = (dir + 1) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]

    x, y = nx, ny

for row in graph:
    print(*row)

print(ty+1, tx+1)