from itertools import combinations
from math import sqrt

def is_prime(num):
    return (len(get_divisors(num)) == 2)
    

def get_divisors(num):
    s = set()
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            s.add(i)
            s.add(num // i)
    return s
    

def solution(nums):
    answer = 0
    count = 0
    for i in combinations(nums, 3):
        if is_prime(sum(i)):
            count += 1 
    
    answer = count
    return answer