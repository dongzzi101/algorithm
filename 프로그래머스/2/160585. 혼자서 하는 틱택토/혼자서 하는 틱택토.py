def solution(board):
    n, m = 3, 3
    
    o_count = 0
    x_count = 0
    
    for y in range(n):
        for x in range(m):
            if board[y][x] == "O":
                o_count += 1
            elif board[y][x] == "X":
                x_count += 1
    
    if x_count > o_count:
        return 0
    if o_count > x_count + 1:
        return 0
    
    def is_win(board, target):
        for i in range(3):
            if all(board[i][j] == target for j in range(3)):
                return True
        
        for j in range(3):
            if all(board[i][j] == target for i in range(3)):
                return True
        
        if all(board[i][i] == target for i in range(3)):
            return True
        if all(board[i][2-i] == target for i in range(3)):
            return True
        
        return False
    
    o_win = is_win(board, "O")
    x_win = is_win(board, "X")
    
    if o_win and x_win:
        return 0
    if o_win and o_count == x_count:
        return 0
    if x_win and o_count > x_count:
        return 0
    
    return 1