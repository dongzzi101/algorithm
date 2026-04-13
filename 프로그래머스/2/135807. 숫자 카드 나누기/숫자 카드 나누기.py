from math import gcd, sqrt
from functools import reduce

def solution(arrayA, arrayB):
    
    def get_divisors(n):
        s = set()
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                s.add(i)
                s.add(n // i)
        return s
    
    def check(x, arr):
        for num in arr:
            if num % x == 0:
                return False
        return True
    
    gcdA = reduce(gcd, arrayA)
    gcdB = reduce(gcd, arrayB)
    
    answer = 0
    
    for d in get_divisors(gcdA):
        if check(d, arrayB):
            answer = max(answer, d)
    
    for d in get_divisors(gcdB):
        if check(d, arrayA):
            answer = max(answer, d)
    
    return answer