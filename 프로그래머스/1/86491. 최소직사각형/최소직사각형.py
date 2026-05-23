def solution(sizes):
    width_max = 0
    height_max = 0
    
    for size in sizes:
        w = max(size)
        h = min(size)
        
        width_max = max(width_max, w)
        height_max = max(height_max, h)
    
    return width_max * height_max