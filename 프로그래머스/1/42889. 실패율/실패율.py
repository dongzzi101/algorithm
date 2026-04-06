def solution(N, stages):
    result = []
    length = len(stages)
    
    for target in range(1, N + 1):
        count = stages.count(target) 
        
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        result.append((target, fail))
        
        length -= count
    
    result.sort(key=lambda x: (-x[1], x[0]))
    
    return [stage for stage, _ in result]