def solution(s):
    answer = []
    
    s = s[2:-2]
    parts = s.split("},{")
    
    parts = [list(map(int, p.split(','))) for p in parts]
    
    parts.sort(key=lambda x: len(x))
    
    seen = set()
    
    for part in parts:
        for num in part:
            if num not in seen:
                answer.append(num)
                seen.add(num)
    
    return answer