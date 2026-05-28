def solution(m, n, board):
    board = [list(row) for row in board]
    answer = 0
    
    while True:
        pang = set()
        
        for y in range(m-1):
            for x in range(n-1):
                target = board[y][x]
                if target != '0' and board[y][x] == board[y+1][x] == board[y][x+1] == board[y+1][x+1]:
                    pang.add((y, x))
                    pang.add((y+1, x))
                    pang.add((y, x+1))
                    pang.add((y+1, x+1))
        
        if not pang:  
            break
            
        answer += len(pang)
        for y, x in pang:
            board[y][x] = '0'
            
        for x in range(n): 
            stack = []
            
            
            for y in range(m):
                if board[y][x] != '0':
                    stack.append(board[y][x])
            
            empty_count = m - len(stack)
            
            for y in range(m):
                if y < empty_count:
                    board[y][x] = '0' 
                else:
                    board[y][x] = stack[y - empty_count]
            
    return answer