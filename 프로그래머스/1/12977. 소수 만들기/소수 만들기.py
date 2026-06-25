from itertools import combinations

def solution(nums):
    
    def is_prime_number(num):
        
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        
        return True
    
    count = 0
    
    for num in combinations(nums, 3):
        
        if is_prime_number(sum(num)):
            count += 1

    return count