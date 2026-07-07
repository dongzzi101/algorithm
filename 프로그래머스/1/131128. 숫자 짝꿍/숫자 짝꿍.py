def solution(X, Y):
    x = list(map(int, X))
    y = list(map(int, Y))
    
    x_map = {}
    y_map = {}
    
    for num in x:
        if num in x_map:
            x_map[num] += 1
        else:
            x_map[num] = 1
            
    for num in y:
        if num in y_map:
            y_map[num] += 1
        else:
            y_map[num] = 1
    
    answer = ''
    
    for num in range(9, -1, -1):
        if num in x_map and num in y_map:
            common_min = min(x_map[num], y_map[num])
            answer += str(num) * common_min
    
    if len(answer) == 0:
        return "-1"
    
    if answer.startswith("0"):
        return "0"
    
    return answer