def is_number(s):
    for ch in s:
        if ch.isalpha():
            return False
    
    return True
        

def solution(s):
    answer = True
    
    size = len(s)
    
    if size != 4 and size != 6:
        return False
    
    answer = is_number(s)
    return answer