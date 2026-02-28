def solution(d, budget):
    answer = 0
    
    d.sort()
    count = 0
    
    for i in range(len(d)):
        if d[i] <= budget:
            budget -= d[i]
            count += 1
        else:
            break
    answer = count
    return answer