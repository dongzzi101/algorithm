from itertools import permutations 

def solution(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    answer = 0
    
    num_list = []
    for num in numbers:
        num_list.append(num)
    
    nums = set()

    for i in range(1, len(num_list) + 1):
        for p in permutations(num_list, i):
            num = int(''.join(p))
            nums.add(num)
    
    for num in nums:
        if is_prime(num):
            answer += 1
    
    return answer