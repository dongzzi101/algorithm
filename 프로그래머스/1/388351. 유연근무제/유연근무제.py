def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        schedule = schedules[i]
        
        hour = schedule // 100
        minute = schedule % 100
        minute += 10
        
        if minute >= 60:
            hour += 1
            minute -= 60
        
        limit_time = hour * 100 + minute
        
        is_perfect = True
        
        for j in range(7):
            current_day = (startday -1 + j) % 7 + 1
            
            if current_day == 6 or current_day == 7:
                continue
            
            if timelogs[i][j] > limit_time:
                is_perfect = False
                break
                
        if is_perfect:
            answer += 1
        
    
    return answer