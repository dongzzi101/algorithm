def solution(s, skip, index):
    answer = ''
    
    for ch in s:
        current_ord = ord(ch)
        moved = 0
        
        while moved < index:
            current_ord += 1
            
            if current_ord > ord('z'):
                current_ord = ord('a')
            
            if chr(current_ord) not in skip:
                moved += 1
    
        answer += chr(current_ord)
    
    return answer