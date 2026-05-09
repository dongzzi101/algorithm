def solution(s):
    answer = ''
    
    parts = s.split(' ')
    
    for part in parts:
        if part:
            answer += part[0].upper()
            answer += part[1:].lower()
        
        answer += ' '
    
    return answer[:-1]