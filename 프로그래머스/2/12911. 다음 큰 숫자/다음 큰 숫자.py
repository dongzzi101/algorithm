def solution(n):
    
    def make_binary(n):
        result = ''
        while n > 0:
            result = str(n % 2) + result
            n //= 2
        return result
    
    def count_one(nums):
        count = 0
        for num in nums:
            if num == '1':
                count += 1
        return count 
    
    target = count_one(make_binary(n))
    
    while True:
        n += 1
        if count_one(make_binary(n)) == target:
            return n