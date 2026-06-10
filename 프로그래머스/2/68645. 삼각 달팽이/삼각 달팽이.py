def solution(n):
    answer = []
    arr = [[i] * i for i in range(1, n+1)]
    
    direction = [(1, 0), (0, 1), (-1, -1)]
    
    row, col = -1, 0
    num = 1
    d = 0
    
    for i in range(n):
        for _ in range(n - i):
            row += direction[d][0]
            col += direction[d][1]
            arr[row][col] = num
            num += 1
    
        d = (d+1) % 3
    
    for i in range(len(arr)):
        answer.extend(arr[i])
    
    
    return answer