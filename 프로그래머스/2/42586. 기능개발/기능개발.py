from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    days = deque()
    
    for progress, speed in zip(progresses, speeds):
        day = math.ceil((100 - progress) / speed)
        days.append(day)
    
    while days:
        current_deploy_day = days.popleft()
        count = 1
        
        while days and days[0] <= current_deploy_day:
            days.popleft()
            count += 1
        
        answer.append(count)
    return answer