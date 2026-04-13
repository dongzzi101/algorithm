from collections import Counter

def solution(weights):
    answer = 0
    count = Counter(weights)
    
    for w in count:
        if count[w] > 1:
            answer += count[w] * (count[w] - 1) // 2
        
        if w * 3 % 2 == 0:
            target = w * 3 // 2
            if target in count:
                answer += count[w] * count[target]
        
        target = w * 2
        if target in count:
            answer += count[w] * count[target]
        
        if w * 4 % 3 == 0:
            target = w * 4 // 3
            if target in count:
                answer += count[w] * count[target]
    
    return answer