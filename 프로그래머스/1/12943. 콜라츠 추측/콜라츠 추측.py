def solution(num):
    answer = 0

    count = 0 
    max_count = 0
    while True:
        if max_count == 500:
            return -1
        
        if num == 1:
            return count
        
        if num % 2 == 0:
            num = num / 2
            count += 1
            max_count += 1
        else:
            num = (3 * num) + 1
            count += 1
            max_count += 1
    
    return answer