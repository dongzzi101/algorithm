import math

def count_divisor(num):
    count = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    return count 

def solution(number, limit, power):
    answer = 0
    fighters = []
    for num in range(1, number+1):
        count = count_divisor(num)
        fighters.append(count)
    
    for fighter in fighters:
        if fighter > limit:
            answer += power
        else:
            answer += fighter
            
    return answer