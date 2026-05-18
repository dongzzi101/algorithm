import math

def solution(progresses, speeds):
    answer = []

    days = []

    for progress, speed in zip(progresses, speeds):
        remain = 100 - progress
        day = math.ceil(remain / speed)
        days.append(day)
        
    current = days[0]
    count = 1
    
    # current = 5 days[1] = 10, days[2] = 1, days[3] = 1, days[4] = 20
    for i in range(1, len(days)):
        if days[i] <= current:
            count += 1
        else:
            answer.append(count)
            current = days[i]
            count = 1

    answer.append(count)

    return answer