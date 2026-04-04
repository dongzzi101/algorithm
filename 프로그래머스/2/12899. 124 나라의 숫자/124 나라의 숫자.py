def solution(n):
    answer = ''
    
    while n > 0:
        n, mod = divmod(n, 3)
        
        if mod == 0:
            answer = '4' + answer
            n -= 1
        elif mod == 1:
            answer = '1' + answer
        else:  
            answer = '2' + answer
    
    return answer