def solution(s):
    s = s[2:-2].split("},{")
    s = sorted(s, key=len)
    
    result = []
    seen = set()
    
    for group in s:
        for num in group.split(","):
            num = int(num)
            
            if num not in seen:
                seen.add(num)
                result.append(num)
    
    return result