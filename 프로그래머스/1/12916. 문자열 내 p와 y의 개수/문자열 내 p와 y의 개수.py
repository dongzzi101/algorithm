def solution(s):
    answer = True
    s = s.lower()
    
    p_count = 0
    y_count = 0
    
    for ch in s:
        if ch == 'p':
            p_count += 1
        
        if ch == 'y':
            y_count += 1
    
    if p_count == y_count:
        answer = True
    else:
        answer = False
    
    return answer