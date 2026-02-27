def get_count_divisor(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    
    return count


def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        count = get_count_divisor(i)
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
    
    return answer