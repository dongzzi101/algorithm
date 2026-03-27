from collections import deque

n = int(input())

board = [[0]*(n+1)]
for _ in range(n):
    board.append([0] + list(map(int, input())))

visited = [[False]*(n+1) for _ in range(n+1)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    q = deque([(y, x)])
    visited[y][x] = True
    count = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 1 <= ny <= n and 1 <= nx <= n:
                if not visited[ny][nx] and board[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    count += 1
    return count

count_list = []

for y in range(1, n+1):
    for x in range(1, n+1):
        if board[y][x] == 1 and not visited[y][x]:
            count_list.append(bfs(y, x))

count_list.sort()

print(len(count_list))
for c in count_list:
    print(c)