def solution(t, p):
    answer = 0
    
    n = len(p)
    count = 0
    for i in range(len(t) - n + 1):
        part_num = t[i:n+i]
        if int(part_num) <= int(p):
            count += 1
            
    answer = count     
    
    return answer