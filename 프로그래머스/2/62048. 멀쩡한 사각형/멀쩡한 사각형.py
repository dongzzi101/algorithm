import math

def solution(w,h):
    answer = 1
    
    normal = w * h
    
    broken = w + h - math.gcd(w, h)
    answer = normal - broken
    
    return answer