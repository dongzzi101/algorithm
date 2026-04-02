def solution(sequence, k):
    
    answer = []
    
    min_len = float('inf')
    
    left = 0
    total = 0
    
    for right in range(len(sequence)):
        total += sequence[right]
        
        while total > k:
            total -= sequence[left]
            left += 1
        
        if total == k:
            if right - left < min_len:
                min_len = right - left
                answer = [left, right]
    
    return answer