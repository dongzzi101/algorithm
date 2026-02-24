N = int(input())
target = int(input())

board = [[0]*N for _ in range(N)]

y = x = N // 2
num = 1
board[y][x] = num

dy = [-1, 0, 1, 0] 
dx = [0, 1, 0, -1]

step = 1
dir = 0

answer_y, answer_x = y, x

while num < N * N:
    for _ in range(2): 
        for _ in range(step):
            if num >= N*N:
                break
            y += dy[dir]
            x += dx[dir]
            num += 1
            board[y][x] = num
            if num == target:
                answer_y, answer_x = y, x
        dir = (dir + 1) % 4
    step += 1

for row in board:
    print(*row)

print(answer_y + 1, answer_x + 1)