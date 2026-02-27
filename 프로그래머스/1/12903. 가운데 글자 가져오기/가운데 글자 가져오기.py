def solution(s):
    answer = ''
    
    n = len(s)
    idx = n // 2
    
    if n % 2 != 0:
        answer = s[idx]
    else:
        answer = s[idx-1:idx+1]
        
    
    return answer