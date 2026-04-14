def solution(m, n, board):
    board = [list(row) for row in board]
    answer = 0
    
    while True:
        to_remove = set()
        
        for y in range(m-1):
            for x in range(n-1):
                if board[y][x] == '.':
                    continue
                
                if board[y][x] == board[y][x+1] == board[y+1][x] == board[y+1][x+1]:
                    print((y,x), (y,x+1), (y+1,x), (y+1,x+1))
                    to_remove.update([
                        (y,x), (y,x+1),
                        (y+1,x), (y+1,x+1)
                    ])
        
        if not to_remove:
            break
        
        answer += len(to_remove)
        for y, x in to_remove:
            board[y][x] = '.'
        
        for x in range(n):
            stack = [board[y][x] for y in range(m) if board[y][x] != '.']
            for y in range(m-1, -1, -1):
                board[y][x] = stack.pop() if stack else '.'
    
    return answer