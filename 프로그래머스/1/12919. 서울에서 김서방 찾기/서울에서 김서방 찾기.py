def solution(seoul):
    answer = ''
    
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = i
            break
    
    return f"김서방은 {answer}에 있다"
