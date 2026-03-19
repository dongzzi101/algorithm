def solution(triangle):
    dp = triangle 

    for y in range(1, len(triangle)):
        for x in range(len(triangle[y])):
            
            if x == 0:
                dp[y][x] += dp[y-1][x]
            
            elif x == y:
                dp[y][x] += dp[y-1][x-1]
            
            else:
                dp[y][x] += max(dp[y-1][x-1], dp[y-1][x])

    return max(dp[-1])