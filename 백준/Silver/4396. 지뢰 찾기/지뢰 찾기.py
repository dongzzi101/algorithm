n = int(input())

pan = []

for i in range(n):
    pan.append(list(input().rstrip()))

player_map = []
for i in range(n):
    player_map.append(list(input().rstrip()))

boom = False

for i in range(n):
    for j in range(n):
        if player_map[i][j] == 'x' and pan[i][j] == '*':
            boom = True

result = [['.'] * n for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(n):
    for j in range(n):

        if player_map[i][j] == 'x':
            if pan[i][j] == '*':
                result[i][j] = '*'
            else:
                cnt = 0
                for d in range(8):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if 0 <= ni < n and 0 <= nj < n:
                        if pan[ni][nj] == '*':
                            cnt += 1
                result[i][j] = str(cnt)

if boom:
    for i in range(n):
        for j in range(n):
            if pan[i][j] == '*':
                result[i][j] = '*'

for row in result:
    print(''.join(row))
