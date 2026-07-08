def solution(x):
    answer = False
    
    digits = list(map(int, str(x)))
    digits_sum = sum(digits)
    
    if int(x) % digits_sum == 0:
        return True
    
    return answer