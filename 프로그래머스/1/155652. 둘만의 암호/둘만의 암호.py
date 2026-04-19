def solution(s, skip, index):
    answer = ''
    skip_set = set(skip) 
    
    for ch in s:
        count = 0
        current = ord(ch)
        
        while count < index:
            current += 1
            
            if current > ord('z'):
                current = ord('a')
            
            if chr(current) in skip_set:
                continue
            
            count += 1
        
        answer += chr(current)
    
    return answer