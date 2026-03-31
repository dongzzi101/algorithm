def solution(s):
    answer = ''
    prev = ' '
    
    for c in s:
        if prev == ' ':
            answer += c.upper()
        else:
            answer += c.lower()
        prev = c
    
    return answer