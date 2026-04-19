def solution(n):
    answer = 0
    
    def ten_to_three(num):
        result = []
        
        while num > 0:
            result.append(str(num % 3))
            num //= 3
    
        return ''.join(reversed(result))
    
    def reverse(num):
        return num[::-1]
    
    def three_to_ten(num):
        result = 0
        
        for digit in num:
            result = result * 3 + int(digit)
        
        return result
    
    result = ten_to_three(n)
    result = reverse(result)
    result = three_to_ten(result)
    
    answer = result
    
    return answer