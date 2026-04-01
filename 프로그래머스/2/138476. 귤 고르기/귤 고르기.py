def solution(k, tangerine):
    box_map = {}

    for t in tangerine:
        if t in box_map:
            box_map[t] += 1
        else:
            box_map[t] = 1
    
    counts = sorted(box_map.values(), reverse=True)
    
    total = 0
    kind = 0
    
    for c in counts:
        total += c
        kind += 1
        
        if total >= k:
            break
    
    return kind
    
        
    
    
    