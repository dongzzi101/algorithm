def solution(numbers, n):
    answer = 0
    number_sum = 0
    
    for number in numbers:
        if number_sum <= n:
            number_sum += number
        answer =  number_sum
    
    return answer