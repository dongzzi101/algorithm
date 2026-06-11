def solution(s):
    answer = 0
    
    same_with_x_count = 0
    diff_with_x_count = 0
    
    temp_x = ""
    
    for char in s:
        if same_with_x_count == 0 and diff_with_x_count == 0:
            temp_x = char
            
        if char == temp_x:
            same_with_x_count += 1
        else:
            diff_with_x_count += 1
            
        if same_with_x_count == diff_with_x_count:
            answer += 1
            same_with_x_count = 0
            diff_with_x_count = 0
            
    if same_with_x_count != 0:
        answer += 1
        
    return answer