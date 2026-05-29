def solution(s, n):
    answer = ''
    
    for ch in s:
        if 65 <= ord(ch) <= 90:
            move = ord(ch) + n
            if move > 90:
                move -= 26
                answer += chr(move)
            else:
                answer += chr(move)
        
        elif 97 <= ord(ch) <= 122:
            move = ord(ch) + n
            if move > 122:
                move -= 26
                answer += chr(move)
            else:
                answer += chr(move)
        else:
            answer += ch
                
    
    return answer