from collections import Counter

def solution(N, stages):
    answer = []
    s_count = Counter(stages)
    participants = len(stages)
    
    fail_rates = []
    
    for i in range(1, N+1):
        if participants == 0:
            fail_rate = 0
        else:
            fail_rate = s_count[i] / participants
        
        fail_rates.append((i, fail_rate))
        participants -= s_count[i]
    
    fail_rates.sort(key=lambda x: (-x[1], x[0]))
    
    for fail_rate in fail_rates:
        stage, _ = fail_rate
        answer.append(stage)
    
    return answer