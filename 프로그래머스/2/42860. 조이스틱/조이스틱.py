def solution(name):
    n = len(name)
    
    answer = 0
    for c in name:
        move = ord(c) - ord('A')
        answer += min(move, 26 - move)
    
    move = n - 1  
    
    for i in range(n):
        next_i = i + 1
        
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        
        move = min(move, i * 2 + (n - next_i), (n - next_i) * 2 + i)
    
    return answer + move