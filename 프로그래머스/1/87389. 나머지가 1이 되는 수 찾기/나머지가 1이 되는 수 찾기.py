def solution(n):
    answer = 0
    answers = []
    
    for i in range(2, n):
        if n % i == 1:
            answers.append(i)
    
    answer = min(answers)    
        
    
    return answer