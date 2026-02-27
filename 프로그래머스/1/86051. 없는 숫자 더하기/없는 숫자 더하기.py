def solution(numbers):
    check = [-1] * 10
    answer = 0
    
    for i in numbers:
        check[i] = i 
    
    for i in range(len(check)):
        if check[i] == -1:
            answer += i
    
    return answer