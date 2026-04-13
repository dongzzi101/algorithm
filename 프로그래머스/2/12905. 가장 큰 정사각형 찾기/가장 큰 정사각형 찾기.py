def solution(board):
    row = len(board)
    col = len(board[0])
    
    dp = [[0] * col for _ in range(row)]
    max_len = 0
    
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    ) + 1
                
                max_len = max(max_len, dp[i][j])
    
    return max_len ** 2