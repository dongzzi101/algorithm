def solution(board, moves):
    def find_doll(move):
        col = move - 1
        
        for row in range(len(board)):
            if board[row][col] != 0:
                value = board[row][col]
                board[row][col] = 0
                return value
        
        return 0
    
    stack = []
    count = 0
    
    for move in moves:
        value = find_doll(move)
        
        if value == 0:
            continue
        
        if stack and stack[-1] == value:
            stack.pop()
            count += 2
        else:
            stack.append(value)
    
    return count