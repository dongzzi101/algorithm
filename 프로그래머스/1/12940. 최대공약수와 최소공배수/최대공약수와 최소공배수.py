from math import sqrt

def get_divisors(num):
    s = set()
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            s.add(i)
            s.add(num // i)
    return s

def get_GCD(a, b):
	set_a = get_divisors(a)
	set_b = get_divisors(b)
	return max(set_a & set_b)

def get_LCM(a, b):
	return (a * b // get_GCD(a, b))

def solution(n, m):
    answer = []
    answer.append(get_GCD(n, m))
    answer.append(get_LCM(n, m))
    
    return answer