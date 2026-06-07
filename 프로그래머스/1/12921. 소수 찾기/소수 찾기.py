def solution(n):
    answer = 0
    
    def is_prime_number(num):
        if num < 2:
            return False
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        
        return True
        
    
    for num in range(1, n+1):
        if is_prime_number(num):
            answer += 1
            
    return answer