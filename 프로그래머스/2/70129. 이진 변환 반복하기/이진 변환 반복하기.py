def solution(s):
    
    def change_bianary(num):
        if num == 0:
            return "0"
    
        result = ""
    
        while num > 0:
            result += str(num % 2)  
            num //= 2               

        return result[::-1]        
    
    answer = []
    
    zero_count = 0
    total_count = 0
    
    while s != "1":
        zero_count += s.count('0')       
        s = s.replace('0', '') 
        
        num = len(s)
        s = change_bianary(num)
        total_count += 1
    
    answer.append(total_count)
    answer.append(zero_count)
    
    return answer