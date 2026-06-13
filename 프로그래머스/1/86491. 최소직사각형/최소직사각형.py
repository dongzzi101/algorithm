def solution(sizes):
    answer = 0
    
    max_w = 1
    max_h = 1
    
    for size in sizes:
        w, h = size
        
        if h > w:
            w, h = h, w
            
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    
    answer = max_w * max_h        
    return answer