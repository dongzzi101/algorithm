from itertools import combinations

def solution(nums):
    answer = 0
    
    def is_prime_num(num):
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True
    
    for comb in combinations(nums, 3):
        if is_prime_num(sum(comb)):
            answer += 1
        
    return answer