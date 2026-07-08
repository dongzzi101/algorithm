def solution(mats, park):
    
    mats.sort(reverse=True)
    
    height = len(park)
    width = len(park[0])
    
    
    for size in mats:
        
        for r in range(height - size + 1):
            for c in range(width - size + 1):
                is_possible = True
                
                for y in range(r, r + size):
                    for x in range(c, c + size):
                        if park[y][x] != "-1":
                            is_possible = False
                            break
                    
                    if not is_possible:
                        break
                    
                if is_possible:
                    return size
    
    return -1