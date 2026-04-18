from functools import reduce

def solution(arr):
    answer = arr[0]
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    for i in arr[1:]:
        answer = lcm(answer, i)
    
    return answer