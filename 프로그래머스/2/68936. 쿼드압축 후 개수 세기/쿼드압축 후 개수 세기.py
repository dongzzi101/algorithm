def solution(arr):
    result = [0, 0]  
    
    def dfs(y, x, size):
        first = arr[y][x]
        
        for i in range(y, y + size):
            for j in range(x, x + size):
                if arr[i][j] != first:
                    
                    half = size // 2
                    
                    dfs(y, x, half)
                    dfs(y, x + half, half)
                    dfs(y + half, x, half)
                    dfs(y + half, x + half, half)
                    
                    return
        
        result[first] += 1
    
    dfs(0, 0, len(arr))
    
    return result