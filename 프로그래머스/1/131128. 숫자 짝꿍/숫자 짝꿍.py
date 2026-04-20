from collections import Counter

def solution(X, Y):
    cx = Counter(X)
    cy = Counter(Y)
    
    result = []
    
    for num in '0123456789':   
        count = min(cx[num], cy[num])
        result.append(num * count)
    
    answer = ''.join(result)
    
    if not answer:
        return "-1"
    
    if set(answer) == {'0'}:
        return "0"
    
    return ''.join(sorted(answer, reverse=True))