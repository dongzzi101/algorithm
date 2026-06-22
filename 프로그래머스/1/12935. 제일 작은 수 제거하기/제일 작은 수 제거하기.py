def solution(arr):
    answer = []
    
    if len(arr) == 1:
        return [-1]
    
    min_num = min(arr)
    
    for num in arr:
        if num == min_num:
            continue
        
        answer.append(num)
                    
    return answer