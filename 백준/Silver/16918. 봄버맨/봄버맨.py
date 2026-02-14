R, C, N = map(int, input().split())


matrix = [list(input()) for _ in range(R)]

def explode(board):
    new_board = [['O'] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if board[r][c] == 'O':
                new_board[r][c] = '.'
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        new_board[nr][nc] = '.'
    return new_board


if N == 1:
    result = matrix

elif N % 2 == 0:
    result = [['O'] * C for _ in range(R)]

elif N % 4 == 3:
    result = explode(matrix)

else:  
    result = explode(explode(matrix))


for row in result:
    print(''.join(row))