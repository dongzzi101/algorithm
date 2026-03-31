def solution(n):
    answer = 0
    
    for start in range(1, n // 2 + 1):
        total = 0
        for i in range(start, n + 1):
            total += i
            if total == n:
                answer += 1
                break
            elif total > n:
                break
    
    return answer + 1 