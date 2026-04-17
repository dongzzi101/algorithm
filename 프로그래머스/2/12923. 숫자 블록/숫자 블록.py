def solution(begin, end):
    answer = []
    
    for n in range(begin, end + 1):
        if n == 1:
            answer.append(0)
            continue
        
        result = 1
        
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                pair = n // i
                
                if pair <= 10_000_000:
                    result = pair
                    break
                else:
                    result = i
        
        answer.append(result)
    
    return answer