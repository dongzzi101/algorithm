def is_prime(num):
    if num == 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

def convert(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1] 

def solution(n, k):
    num_string = convert(n, k)
    nums = num_string.split('0')
    
    answer = 0
    for num in nums:
        if num != '':
            answer += is_prime(int(num))

    return answer